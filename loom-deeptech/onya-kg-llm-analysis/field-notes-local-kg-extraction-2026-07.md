# Field notes: baking off local LLMs for knowledge-graph extraction

**July 2026 edition**

*Companion to ["Building and working knowledge graphs with Onya and LLMs."](https://loom.ogbuji.net/tech/building-and-working-knowledge-graphs-with-onya-and-local-llms/) The main article shows the
pipeline that works. This is the lab notebook behind it—every model that left claw marks on me, where and how things broke, and the numbers. If you're choosing a local model for structured extraction, the failures here should
save you a weekend.*

## Setup

Task: extract a character-and-relationship graph from *The Interesting Narrative of the Life of Olaudah
Equiano* (1789)—~440k characters of narrative after trimming the Gutenberg boilerplate and the book's
own front matter (title page, subscriber roll, contents). Chunk to ~12k tokens, prompt each chunk to emit
[Onya Literate](https://github.com/OoriData/Onya), validate by parsing (feeding parse errors back for
repair), form a union of the chunks into one graph under stable IRI identity. Everything to run local: models served via
[oMLX](https://github.com/jundot/omlx) on Apple Silicon—a laptop and a beefier remote Mac.

Everything below is reproducible from the `model_assessment/` harness in the repo. It takes a model id,
runs the full pipeline, and scores the result.

## How I scored "is this graph any good"

**Recall of known relationships, not "accuracy."** I hand-curated ~14 well-attested human-to-human
relationships from the book (Equiano ↔ Pascal, Equiano ↔ Robert King, Phipps ↔ Lutwidge,…) and measured
how many a model's graph actually connects with an edge. I then measured recall within this curated subset, good enough for a quick bake-off.

**Matching should be alias-aware.** The difficulty of this task is that models extract the same
person's name in different ways. The author alone shows up as `GustavusVassa`, `Equiano`, and `Olaudah`; seemingly separate
nodes. The scorer must resolve name variants to one entity, strip honorifics (`Capt. Pascal` →
`pascal`), and count a relationship as recalled if *any* node matching person A shares an edge with *any*
node matching person B.

## Finding 1: Entities are easy; relationships not so much

I found that `Qwen3.5-4B`, both in 4-bit and 8-bit quant, extracted *entities*
beautifully—clean HumpCase ids, sensible types, good coverage. And then it emits **essentially zero
useful edges**. The relationships are all there in the descriptions it writes ("Purchased Equiano from his
master in Virginia") but they never become graph edges; the handful of edges it does emit are not in the desired shape
(`knows -> London` is idiomatic in English, sure, but is not what we're going for). A full-book run produced a 350-node graph with ~8 edges, most of them junk, and a
person-subgraph that was pure dust; no connected component worth the name.

No amount of prompting fixed this (see Finding 5). Pulling entities out of text is a pattern-match; wiring
the *relationships between them* is a reasoning task, and this 4B model can't pull it off. If all you need is The Domesday Book, a 4B can be a decent census taker, but for the KG we needed a bigger engine.

## Finding 2: Speculative decoding (MTP) torpedoed the Qwen MoE

I landed on `Qwen3.6-35B-A3B` for the reference model. It's mixture-of-experts model, 35B params total but ~3B
active per token, so it reasons like something much larger while generating at small-model speed, and
still runs air-gapped on a 32GB Mac.

An 8-bit build of it, served with **multi-token / speculative decoding ("mtp")** on, fell into a
**repetition loop on one chunk** and emitted **623 empty `# Negro<word>` node blocks** — `NegroChat`,
`NegroCherish`, `NegroChief`, on and on. A bit too close to Richard Pryor for us. The graph ballooned to 915 nodes (from a clean ~300), the run
took **20 minutes**, needed repair rounds, and skipped a chunk. Recall: 10/14.

Same weights, same 8-bit, but with **mtp off**:

| | mtp **on** | mtp **off** |
|---|---|---|
| total nodes | 915 | **414** |
| degenerate `Negro*` nodes | 623 | **2** |
| wall-clock | 1249s | **486s** (2.6× faster) |
| skipped chunks / repairs | 1 skip, many retries | **0 skips, every chunk first-try** |
| recall | 10/14 | 10/14 |

`mtp` was pure downside for this workload: slower, unstable, no recall benefit. One possible conclusion is that speculative decoding trades correctness-of-tail for speed, and structured extraction over long inputs is exactly where the tail matters. Another is just that the MTP setup I had on oMLX was buggy. More recent release changelogs do hint at the latter.

## Finding 3: Same weight class, opposite competence: Gemma vs Qwen

Both models I leaned on are mid-size MoEs of similar active size: Qwen `35B-A3B` (~3B active) and Gemma
`4-26B-A4B` (~4B active). You'd expect similar results, but no.

- **Qwen 35B-A3B** felt *balanced*: 10–12/14 recall, ~100–125 person-edges, a connected core of 40–50
  people. It builds a graph.
- **Gemma 4 26B-A4B** proved a spectacular *entity* extractor, but a poor *relationship* extractor. On a full
  run it found **all 14** people in our gold QA set; both endpoints of every relationship, but it wired **only 6 of them**.
  Recall 6/14, 23 person-edges, a largest cluster of 10. **Every single miss was a near miss**: person A
  present, person B present, no edge between them.

That failure shape—perfect entities, absent edges—is *under-linking*, and it's a distinct competence
axis from raw knowledge or entity coverage. Two models can tie on "did it find the people" and diverge
completely on "did it connect them." When you bake off models, measure the edges alongside the node count.

## Finding 4: Quantization loss isn't linear

To be fair I was aware of this before, but it was interesting to note that the small from 6-bit to 8-bit on the same Qwen MoE didn't improve extraction: 6-bit scored 12/14, 8-bit (no mtp) scored 10/14. This difference is probably within run-to-run variance, and if anything the *lower*-precision
build edged it. Precision-of-weights is not the first lever I'd pull for this task; model *family and size* matter more.

## Finding 5: Prompt tuning didn't help much; and the "pink elephant" reification effect

My first thought on the under-linking in Findings 1 and 3 was prompt tweaking. I ran a matrix of prompt
variants against the lean baseline:

- **v2 (heavier):** a "MOST IMPORTANT RULE—RELATIONSHIPS," an "emit BOTH edge and description when in
  doubt," a broadened relation vocabulary, and an explicit self-check pass. On the 35B it **regressed
  recall 10 → 7** and produced **60 `[Relationship]` nodes**. The model, badgered about relationships,
  started *reifying them as nodes* instead of emitting edges.
- **v3 (lighter):** baseline plus two extra relation labels and a single sentence *forbidding*
  `[Relationship]` nodes. On Gemma it **regressed recall 6 → 3** and still produced **23 `[Relationship]`
  nodes**, despite the explicit prohibition.

That's the punchline: **merely mentioning relationship-nodes, even to forbid them, seems to implant the idea.**
Every prompt that raised the concept's salience, by emphasis *or* by prohibition, caused unwanted reification. The
baseline, which never names the concept and just shows edge syntax by example, did not. It's the "don't
think of a pink elephant" effect in prompt form. For this task keeping prompts lean and
example-driven worked better than a ton of Thou Shall Nots. This seems especially so with smaller models, which exhibit *prompt-fragility*, where the same prompt that behaves on one chunk can send them into a loop on the next.

Across every experiment, **the lean baseline won.** So much for naive prompt engineering in this case.
One nice touch is that maintaining the prompts in [WordLoom](https://github.com/OoriData/WordLoom/)
files (see the harness) made it easy to run these experiments over a handful of clean A/B runs.

## Finding 6: Reasoning models fight structured output

Qwen 3.5/3.6 are reasoning models by default. Left alone they prepend a chatty "Thinking Process:\n\n1.
Analyze the request…" preamble to every response, which (a) is slow, and (b) is exactly the preamble that
breaks the parse, so *every* chunk fails first parse and burns the repair budget. Things improved when I disabled
thinking. That would be `extra_body={'chat_template_kwargs': {'enable_thinking': False}}` for oMLX/vLLM; or Ollama's `think: false`; backends vary). With thinking off, the same model emitted raw Onya Literate cleanly and ~5× faster.
If you're wiring a reasoning model into a structured-output loop, try first with its thinking switch off.

## Finding 7: The graph plainly shows the model's warts

Two flavors of noise are worth expecting, because a good graph model surfaces them rather than hiding
them:

- **Aliasing.** The author appears as `GustavusVassa` (the dominant hub, degree 87), `Equiano`, and
  `Olaudah`—three nodes for one man, because a slaver's imposed name and his birth name occur in
  different chunks. This is a hard identity problem, and no system solves it for free; treated as
  a reconciliation task for a second pass, and it's visible right in the rendered figure.
- **Mis-typing.** Smaller and shakier models type ships (`Charming Sally`, `Andromache`, `Carcass`) and
  places (`Jamaica`) as `Person`, and some invent types outside the allowed set (`[Ship]`, `[Event]`,
  even `[Relationship]` per Finding 5). Cheap to filter for a figure by name; a sign the model is guessing
  at types.

The analytical reality of a memoir such as Equiano's is that it's an **ego network**. The author's node tops every centrality
measure, and *removing* the ego
shatters the graph, because most people connect only thereby. The structure that survives is in the
communities detected *with* the ego present: the Robert King trading circle in Montserrat, the officers of
the 1773 Phipps expedition toward the North Pole (Phipps and Lutwidge), the knot of names around the
London kidnapping of Equiano's friend John Annis. Real circles of a real life, pulled out of an 18th-
century autobiography by a 4-billion-active-parameter model running on a laptop. Not bad!

## The runs, in one table

Recall is over the 14-relationship gold set; person-edges and "giant" (largest connected people-cluster)
measure connectivity; all full-book runs unless noted. `A3B`/`A4B` = active-parameter MoE size.

| Model | Quant / serving | Prompt | Recall | Person-edges | Giant | Skips | Wall | Note |
|---|---|---|---:|---:|---:|---:|---:|---|
| Qwen 3.5 **4B** | 4/8-bit | baseline | ~0 usable | ~0 | — | — | — | entities only; no real edges |
| Qwen 3.6 **35B-A3B** | **6-bit** | baseline | **12/14** | 125 | 47 | 2/10 | — | reference — shipped in the article |
| Qwen 3.6 35B-A3B | 8-bit, **mtp on** | baseline | 10/14 | 124 | 50 | 1/10 | 1249s | 623 degenerate nodes (repetition loop) |
| Qwen 3.6 35B-A3B | 8-bit, **mtp off** | baseline | 10/14 | 100 | 41 | 0/10 | 486s | clean, fast, stable |
| Qwen 3.6 35B-A3B | 8-bit, mtp off | v2 (heavy) | 7/14 | 64 | 21 | 0/10 | 1439s | 60 `[Relationship]` nodes |
| Gemma **4 26B-A4B** | 8-bit | baseline | 6/14 | 23 | 10 | 2/10 | 863s | entity-perfect, pure under-linker |
| Gemma 4 26B-A4B | 8-bit | v3 (light) | 3/14 | 11 | 6 | 2/10 | 505s | 23 `[Relationship]` nodes |

*The harness, the gold set, the prompt variants, and every result above are in `model_assessment/`. Bring
your own model and an OpenAI-compatible inference endpoint; the reports are directly comparable.*
