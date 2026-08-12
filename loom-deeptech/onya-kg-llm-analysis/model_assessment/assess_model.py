#!/usr/bin/env python
'''One-shot bake-off for a local model on the Equiano knowledge-graph extraction task.

Point it at any OpenAI-compatible endpoint and a model id; it runs the full chunk -> extract -> repair ->
union pipeline over the pre-processed narrative, then reports:

  * runtime      — total wall-clock and per-chunk timings
  * robustness   — how many chunks the model never got to parse (skipped after retries)
  * graph shape  — nodes, people, edges, giant-component size, community count
  * quality      — RECALL against a curated set of known human-to-human relationships
                   (see gold_relationships.py), the metric that actually tracks "is this graph any good"

Everything is written to model_assessment/results/<model>/ : a markdown report, the extracted Onya
Literate, and each chunk's raw model output (for eyeballing failures).

Prerequisites:
    pip install 'onya[nx]' openai httpx
    python fetch_equiano.py            # once, to produce equiano_narrative.txt

Usage:
    python assess_model.py mlx-community/Qwen3.6-35B-A3B-6bit
    python assess_model.py gemma-4-31b --base-url http://localhost:8800/v1 --api-key oori --limit 3
'''
import argparse
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI

from onya.graph import graph
from onya.serial import literate, nx
from onya.serial.literate import LiterateParser

import gold_relationships as gold
import prompts   # local WordLoom loader (prompts/__init__.py)

HERE = Path(__file__).parent
NARRATIVE = HERE / 'equiano_narrative.txt'
DOC_IRI = 'https://example.org/books/equiano-narrative'
NODEBASE = DOC_IRI + '/'


def chunks(text, size):
    for i in range(0, len(text), size):
        yield text[i:i + size]


class Extractor:
    '''Runs the extract-with-repair loop for one model. Prompts come from a WordLoom file so they can be
    swapped per experiment (--prompt-file); thinking mode is selectable (--thinking).'''

    def __init__(self, client, model, max_tokens, prompt_file, think_mode):
        self.client, self.model, self.max_tokens = client, model, max_tokens
        self.prompt_file = prompt_file
        self.think_mode = think_mode              # 'off' | 'on' | 'auto'
        self._switch_ok = think_mode != 'auto'    # send enable_thinking unless auto; latch off on reject

    def complete(self, messages):
        kw = dict(model=self.model, messages=messages, temperature=0.0, max_tokens=self.max_tokens)
        if self._switch_ok:
            try:
                return self.client.chat.completions.create(
                    **kw, extra_body={'chat_template_kwargs': {'enable_thinking': self.think_mode == 'on'}}
                ).choices[0].message.content
            except Exception:  # noqa: BLE001 — endpoint rejected the switch; fall back to model default
                self._switch_ok = False
        return self.client.chat.completions.create(**kw).choices[0].message.content

    def extract(self, chunk, retries=2):
        '''Return (graph_or_None, attempts, last_text). None graph == skipped after retries.'''
        prompt = str(prompts.load(self.prompt_file, 'kg-extract').render(
            doc_iri=DOC_IRI, nodebase=NODEBASE, chunk=chunk))
        messages = [{'role': 'user', 'content': prompt}]
        text = ''
        for attempt in range(retries + 1):
            text = self.complete(messages)
            g = graph()
            try:
                LiterateParser().parse(text, g)
                return g, attempt + 1, text
            except Exception as e:  # noqa: BLE001
                # Onya 0.4.2's parser errors name the offending token and the fix, so the exception fed
                # straight back (via the kg-repair prompt) is enough to repair with.
                repair = str(prompts.load(self.prompt_file, 'kg-repair').render(error=str(e)))
                messages += [{'role': 'assistant', 'content': text},
                             {'role': 'user', 'content': repair}]
        return None, retries + 1, text


# --- gold-relationship scoring -------------------------------------------------------------------

def toks(s):
    '''Tokenise a name/id: split HumpCase, drop punctuation and honorifics, lower-case.'''
    s = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', s)
    parts = re.split(r'[^A-Za-z0-9]+', s.lower())
    return {p for p in parts if p and p not in gold.HONORIFICS}


ENTITY_ALIASES = {k: [toks(a) for a in variants] for k, variants in gold.ENTITIES.items()}


def node_token_index(g):
    '''node-id -> token set, from the id tail and every schema:name value.'''
    NAME = 'https://schema.org/name'
    idx = {}
    for n in g.values():
        nid = str(n.id)
        t = toks(nid.rsplit('/', 1)[-1])
        for p in n.properties:
            if str(p.label) == NAME:
                t |= toks(str(p.value))
        idx[nid] = t
    return idx


def entities_to_nodes(idx):
    out = {}
    for key, alias_sets in ENTITY_ALIASES.items():
        out[key] = {nid for nid, nt in idx.items()
                    if any(a and a <= nt for a in alias_sets)}
    return out


def score_relationships(g):
    import networkx
    mg = nx.to_networkx(g).to_undirected()
    idx = node_token_index(g)
    ent_nodes = entities_to_nodes(idx)
    results = []
    for a, b, note in gold.RELATIONSHIPS:
        na, nb = ent_nodes[a], ent_nodes[b]
        found = any(mg.has_edge(x, y) for x in na for y in nb if x != y)
        results.append({'a': a, 'b': b, 'note': note,
                        'a_present': bool(na), 'b_present': bool(nb), 'edge_found': found})
    return results, ent_nodes


# --- reachability: which relationships are even *available* in the text processed ------------------
# A partial run (--limit) only sees the front of the book, so most gold relationships are unreachable
# through no fault of the model. In the Olaudah Equiano book, for example, Robert King and Montserrat
# arrive after a half dozen chapters, and the abolitionists not until near the end.
# We locate roughly where each party first appears (by distinctive name mention) and call a relationship reachable
# once BOTH parties' first mention falls inside the processed span. This is a heuristic. It keys off name spellings
# in the source text, but it reliably separates "the model missed this" from "this person doesn't show up until chapter 9".


OFFSET_SKIP = {'farmer'}  # bare common-noun tokens too ambiguous to locate a person by


def entity_first_offset(book_lower, entity_key):
    if entity_key == gold.NARRATOR:
        return 0   # the first-person narrator is present from the start, whatever the text calls him
    best = None
    for variant in gold.ENTITIES[entity_key]:
        v = variant.lower()
        if v in OFFSET_SKIP:
            continue
        m = re.search(r'\b' + re.escape(v) + r'\b', book_lower)
        if m and (best is None or m.start() < best):
            best = m.start()
    return best


def reachability(book, chars_processed):
    '''(entity_a, entity_b) -> True (reachable) / False (appears later) / None (name not found).'''
    bl = book.lower()
    first = {k: entity_first_offset(bl, k) for k in gold.ENTITIES}
    out = {}
    for a, b, _ in gold.RELATIONSHIPS:
        oa, ob = first[a], first[b]
        out[(a, b)] = None if oa is None or ob is None else (max(oa, ob) < chars_processed)
    return out


# --- report --------------------------------------------------------------------------------------

def kg_stats(g):
    import networkx
    people = {str(n.id) for n in g.typematch('https://schema.org/Person')}
    full = nx.to_networkx(g)
    psub = full.subgraph(people)
    giant = max((len(c) for c in networkx.connected_components(psub.to_undirected())), default=0)
    return {'nodes': len(g), 'people': len(people), 'edges': full.number_of_edges(),
            'person_edges': psub.number_of_edges(), 'giant_people': giant}


def write_report(out_dir, model, cfg, per_chunk, wall, g, rel_results, reach, full_run):
    stats = kg_stats(g)
    recalled = sum(r['edge_found'] for r in rel_results)
    skipped = sum(1 for c in per_chunk if c['status'] == 'SKIPPED')
    reachable = [r for r in rel_results if reach.get((r['a'], r['b'])) is True]
    rec_reach = sum(r['edge_found'] for r in reachable)
    mark = {True: '✓', False: '·', None: '?'}

    lines = []
    lines.append(f'# Model assessment — `{model}`\n')
    think = cfg['think_mode'] + ('' if cfg['switch_ok'] else ' (switch unsupported → model default)')
    lines.append(f'*{cfg["timestamp"]}*  ·  endpoint `{cfg["base_url"]}`  ·  '
                 f'prompt `{cfg["prompt_file"]}`  ·  thinking `{think}`  ·  '
                 f'chunk {cfg["chunk_chars"]:,} chars  ·  max_tokens {cfg["max_tokens"]}\n')
    if not full_run:
        lines.append(f'> **Partial run** — only the first {len(per_chunk)} chunk(s) '
                     f'(~{cfg["chars_processed"]:,} of {cfg["book_chars"]:,} chars, '
                     f'{100*cfg["chars_processed"]/cfg["book_chars"]:.0f}% of the book) were processed. '
                     f'Judge quality by **recall among reachable relationships**, not the all-gold '
                     f'number: most gold relationships involve people who only appear later in the book.\n')
    lines.append('## Headline\n')
    lines.append(f'| metric | value |')
    lines.append(f'|---|---|')
    lines.append(f'| wall-clock | {wall:.0f}s ({wall/60:.1f} min) |')
    lines.append(f'| chunks skipped | {skipped} / {len(per_chunk)} |')
    lines.append(f'| **relationship recall (reachable)** | **{rec_reach} / {len(reachable)}** |')
    lines.append(f'| relationship recall (all gold) | {recalled} / {len(rel_results)} |')
    lines.append(f'| nodes / people | {stats["nodes"]} / {stats["people"]} |')
    lines.append(f'| edges (all / person-person) | {stats["edges"]} / {stats["person_edges"]} |')
    lines.append(f'| largest connected people-cluster | {stats["giant_people"]} |')
    lines.append('')
    lines.append('## Relationship recall (gold set)\n')
    lines.append('`in text?`: ✓ both parties appear within the processed span · `·` a party appears '
                 'only later in the book (unreachable here) · `?` a party\'s name was not located.\n')
    lines.append('| A | B | A found? | B found? | in text? | edge? | relationship |')
    lines.append('|---|---|:--:|:--:|:--:|:--:|---|')
    for r in rel_results:
        lines.append(f'| {r["a"]} | {r["b"]} | {"✓" if r["a_present"] else "·"} | '
                     f'{"✓" if r["b_present"] else "·"} | {mark[reach.get((r["a"], r["b"]))]} | '
                     f'{"**✓**" if r["edge_found"] else "·"} | {r["note"]} |')
    lines.append('')
    lines.append('## Per-chunk\n')
    lines.append('| chunk | chars | attempts | status | nodes after | time |')
    lines.append('|---|---|---|---|---|---|')
    for c in per_chunk:
        lines.append(f'| {c["i"]} | {c["chars"]:,} | {c["attempts"]} | {c["status"]} | '
                     f'{c["nodes_after"]} | {c["time"]:.0f}s |')
    lines.append('')
    (out_dir / 'report.md').write_text('\n'.join(lines))
    return {'recalled': recalled, 'rec_reach': rec_reach, 'n_reachable': len(reachable),
            'skipped': skipped, 'stats': stats}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('model', help='model id as the endpoint knows it')
    ap.add_argument('--base-url', default=os.environ.get('ONYA_LLM_BASE_URL', 'http://localhost:8800/v1'))
    ap.add_argument('--api-key', default=os.environ.get('ONYA_LLM_KEY', 'local'))
    ap.add_argument('--chunk-chars', type=int, default=12_000 * 4)
    ap.add_argument('--max-tokens', type=int, default=8000)
    ap.add_argument('--retries', type=int, default=2)
    ap.add_argument('--limit', type=int, default=None, help='cap chunks (smoke test)')
    ap.add_argument('--prompt-file', default='extract.loom.toml',
                    help='WordLoom file under prompts/ (copy extract.loom.toml to A/B a variant)')
    ap.add_argument('--thinking', choices=['off', 'on', 'auto'], default='off',
                    help="reasoning mode: off (default), on, or auto (send no switch, use model default)")
    args = ap.parse_args()

    if not NARRATIVE.exists():
        raise SystemExit(f'{NARRATIVE} missing — run `python fetch_equiano.py` first.')
    book = NARRATIVE.read_text()

    # Output dir carries the experiment axes so runs of the same model with different prompt/thinking
    # don't clobber each other. Defaults keep the plain results/<model>/ path (back-compatible).
    parts = [re.sub(r'[^A-Za-z0-9._-]+', '_', args.model)]
    if args.prompt_file != 'extract.loom.toml':
        parts.append(Path(args.prompt_file).stem)
    if args.thinking != 'off':
        parts.append(f'think-{args.thinking}')
    out_dir = HERE / 'results' / '__'.join(parts)
    (out_dir / 'raw').mkdir(parents=True, exist_ok=True)

    client = OpenAI(base_url=args.base_url, api_key=args.api_key)
    ex = Extractor(client, args.model, args.max_tokens, args.prompt_file, args.thinking)

    g = graph()
    per_chunk = []
    t0 = time.time()
    for i, chunk in enumerate(chunks(book, args.chunk_chars)):
        if args.limit is not None and i >= args.limit:
            break
        tc = time.time()
        cg, attempts, text = ex.extract(chunk, retries=args.retries)
        (out_dir / 'raw' / f'chunk{i:02d}.md').write_text(text)
        if cg is None:
            status = 'SKIPPED'
        else:
            g.union(cg)
            status = 'ok'
        rec = {'i': i, 'chars': len(chunk), 'attempts': attempts, 'status': status,
               'nodes_after': len(g), 'time': time.time() - tc}
        per_chunk.append(rec)
        print(f'chunk {i}: {status} in {rec["time"]:.0f}s ({attempts} attempts) -> {len(g)} nodes',
              flush=True)
    g.merge()
    wall = time.time() - t0

    with open(out_dir / 'extracted.onya.md', 'w') as fp:
        literate.write(g, fp, document=DOC_IRI, nodebase=NODEBASE, schema='https://schema.org/')

    rel_results, ent_nodes = score_relationships(g)
    chars_processed = sum(c['chars'] for c in per_chunk)
    full_run = chars_processed >= len(book)
    reach = reachability(book, chars_processed)
    cfg = {'base_url': args.base_url, 'chunk_chars': args.chunk_chars, 'max_tokens': args.max_tokens,
           'prompt_file': args.prompt_file, 'think_mode': args.thinking, 'switch_ok': ex._switch_ok,
           'chars_processed': chars_processed, 'book_chars': len(book),
           'timestamp': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}
    res = write_report(out_dir, args.model, cfg, per_chunk, wall, g, rel_results, reach, full_run)

    print(f'\n=== {args.model} ===')
    scope = 'full book' if full_run else f'{100*chars_processed/len(book):.0f}% of book'
    print(f'wall {wall:.0f}s | skipped {res["skipped"]}/{len(per_chunk)} | '
          f'recall {res["rec_reach"]}/{res["n_reachable"]} reachable '
          f'({res["recalled"]}/{len(rel_results)} all gold, {scope}) | '
          f'people {res["stats"]["people"]} | person-edges {res["stats"]["person_edges"]} | '
          f'giant {res["stats"]["giant_people"]}')
    print(f'report: {out_dir / "report.md"}')


if __name__ == '__main__':
    main()
