# Model assessment harness

A one-shot bake-off for choosing a *local* model capable of extracting a decent knowledge graph from
*The Interesting Narrative of the Life of Olaudah Equiano*, for the article "Building and working
knowledge graphs with Onya and LLMs". Point it at any OpenAI-compatible endpoint and a model id; it runs
the real chunk → extract → repair → union pipeline and scores the result.

## Why this exists

Extraction quality degrades ungracefully as models shrink. In testing, a 4B model produced clean
entities but almost no relationship *edges*; a 35B-A3B MoE wired the relationships together but still
mis-typed some ships/places as people. This harness makes that trade-off measurable so you can shop for
a model that's good enough to ship a nicer version of the article — especially on a beefier remote Mac
with lighter quantization.

## Files

| File | Purpose |
|------|---------|
| `fetch_equiano.py` | Download + pre-process the book into `equiano_narrative.txt` (strips Gutenberg boilerplate and the book's front matter). Run once. |
| `equiano_narrative.txt` | The cleaned narrative the harness extracts from (produced by the fetch script). |
| `gold_relationships.py` | Hand-curated, alias-aware ground truth: known human-to-human relationships to score recall against. |
| `prompts/extract.loom.toml` | The extraction + repair prompts, as a [WordLoom](https://github.com/OoriData/WordLoom/) file. Copy it to make a prompt-experiment variant. |
| `prompts/__init__.py` | Small WordLoom loader (`import prompts`). |
| `assess_model.py` | The harness. Takes a model id, runs extraction, writes a report. |
| `results/<model>[__variant]/` | Per-run output: `report.md`, `extracted.onya.md`, and `raw/chunkNN.md` (raw model output per chunk, for eyeballing failures). |

## Setup

```sh
pip install 'onya[nx]>=0.4.2' openai httpx wordloom
python fetch_equiano.py          # once — writes equiano_narrative.txt
```

## Run

```sh
# defaults to endpoint http://localhost:8800/v1 (override with --base-url / --api-key or the
# ONYA_LLM_BASE_URL / ONYA_LLM_KEY env vars)
python assess_model.py mlx-community/Qwen3.6-35B-A3B-6bit
python assess_model.py gemma-4-31b-it --base-url http://REMOTE:8800/v1 --api-key KEY
python assess_model.py some-model --limit 3        # smoke test: first 3 chunks only
```

Useful flags: `--chunk-chars` (default 48000 ≈ 12k tokens), `--max-tokens` (default 8000),
`--retries` (default 2), `--limit` (cap chunks).

### Prompt and thinking experiments

The prompts live in `prompts/extract.loom.toml`, not in the Python — so you can A/B them without
touching code. Two axes:

- **`--prompt-file NAME`** — load prompts from a different loom file under `prompts/`. Copy the baseline,
  edit the `[kg-extract]` / `[kg-repair]` sections, and compare:
  ```sh
  cp prompts/extract.loom.toml prompts/extract-v2.loom.toml   # then edit it
  python assess_model.py MODEL --prompt-file extract-v2.loom.toml
  ```
- **`--thinking {off,on,auto}`** — reasoning mode. `off` (default) sends `enable_thinking=False`; `on`
  sends `True`; `auto` sends no switch and takes the model's default. Useful for testing whether a
  reasoning model does better with thinking on (at the cost of speed, and a preamble the repair loop
  has to survive).

Each run records the prompt file and thinking mode in the report header, and non-default runs land in
`results/<model>__<promptstem>__think-<mode>/` so experiments don't clobber each other. That makes a
clean model × prompt × thinking matrix, all comparable via the same recall metric.

> ### ⚠️ `--limit` and the recall number — read this
> `--limit N` only feeds the model the **first N chunks**, i.e. the front of the book. But the gold
> relationships are spread across the *whole* narrative — Robert King and Montserrat come around the
> midpoint, the Phipps Arctic voyage and the London abolitionists (Sharp, Clarkson, Annis) near the
> end. So a limited run **cannot** recall relationships whose people haven't appeared yet, and the raw
> "X / 14" would unfairly punish the model.
>
> The report handles this with a **reachability** column. It locates roughly where each person first
> appears in the source text (by distinctive name mention; the first-person narrator counts from the
> start) and marks each relationship:
> - `✓` **reachable** — both people appear within the processed span, so the model had a fair shot
> - `·` **later** — a party only shows up further into the book; unreachable in this run
> - `?` — a party's name wasn't located in the text (heuristic limitation)
>
> **Judge a limited run by "relationship recall (reachable)", never by "all gold".** For example, a
> 3-chunk run of one model scored `3 / 6 reachable` (fair) versus `3 / 14 all gold` (misleading). For a
> real cross-model verdict, do a **full run (drop `--limit`)** — then reachable ≈ all gold and the two
> numbers converge. Reachability is a heuristic keyed off name spellings in the source, so treat it as
> approximate, especially for names that collide with common nouns.

## What it reports (`results/<model>/report.md`)

- **wall-clock** total and per-chunk timings
- **chunks skipped** — how many the model never got to parse-clean, even after repair retries
- **graph shape** — nodes, people, all edges, person-person edges, largest connected people-cluster
- **relationship recall** — of the known relationships in `gold_relationships.py`, how many the model's
  graph connects with an edge. Reported two ways: **recall (reachable)** — the headline quality number,
  scored only over relationships whose people appear in the processed text — and **recall (all gold)**,
  the raw count over all 14 (only equal to reachable on a full run).

Recall is deliberately the primary metric: it tracks "did the model build a usable social graph"
without needing every emitted edge hand-labelled. Matching is lenient and alias-aware (it resolves
*Gustavus Vassa* / *Equiano* / *Olaudah* to one person, and strips honorifics), so it rewards a model
for connecting the right people even when it names them inconsistently. It does **not** measure
precision (spurious edges) or mis-typing directly — skim `extracted.onya.md` for those.

## Interpreting results

A shippable-for-the-article model should, roughly: skip ≤1–2 chunks, recall most of the *reachable*
gold relationships (the 35B-A3B MoE reference run hit 12/14 on a full run), and keep the people in one
large connected component rather than a scatter of isolated mentions.

Two diagnostic patterns to watch in the relationship table:
- **A ✓ · B ✓ · in-text ✓ · edge ·** (both people extracted, present in the text, but no edge between
  them) — the model is capturing entities but leaving relationships in prose descriptions instead of
  wiring them. This *under-linking* is the most common quality ceiling for smaller models; a model with
  many such rows will produce a sparse, hard-to-cluster graph.
- **high recall but a noisy figure** — usually mis-typing (ships/places tagged as people). Cheap to
  filter for a figure, but a sign the model is guessing at types. Skim `extracted.onya.md` to gauge it.
