[ ![Loomiverse](https://storage.ghost.io/c/82/c0/82c0f4a1-bd31-487c-9c3e-cb9f780d0874/content/images/2022/08/Nchefu-Road-cover-banner---shorter.png) ](https://loom.ogbuji.net)

Jul 30, 2026 · 16 min read · [ deep-tech ](https://loom.ogbuji.net/tag/deep-tech/)

# Building and working knowledge graphs with Onya and local LLMs

*Knowledge graphs are powerful tools for GenAI context. Learn how to work with them using a small, private/local model, building knowledge structure from large documents, and treating the graph as a full-blown system of record, rather than a snapshot. ![Building and working knowledge graphs with Onya and local LLMs](https://storage.ghost.io/c/82/c0/82c0f4a1-bd31-487c-9c3e-cb9f780d0874/content/images/size/w960/2026/07/tfa_web-1.png) Tiny fragment of a knowledge graph from Chinua Achebe's novel, _Things Fall Apart_*

_You may not need a frontier cloud model to turn a shelf of documents into a knowledge graph. You can get a long way with a basic, local model and a commodious output format. You can go even further with a graph that serves as an actual system of record, rather than a snapshot to be thrown away. You can have all this without any potentially private information leaving your laptop._

Laurent Picard recently published an interesting article, [Building Knowledge Graphs with Gemini](https://hackernoon.com/building-knowledge-graphs-with-gemini?ref=loom.ogbuji.net). He presented code to prompt an LLM to extract entity/relationship graphs from large texts—entire books. My interest in knowledge graphs goes back to the turn of the millennium, so I'm glad to see the continued currency in the LLM age. I'm going to walk similar ground here, but with a couple of switch-ups.

![](https://storage.ghost.io/c/82/c0/82c0f4a1-bd31-487c-9c3e-cb9f780d0874/content/images/2026/07/image.png) Knowledge Graph diagram from Laurent Picard's article

Firstly: no cloud models. I'll be running inference on my own machine, invoking a local model through the plain OpenAI-style API, so everything here works with whatever local stack you prefer: llama.cpp server, vLLM, LM Studio, Ollama, etc. My own daily driver is [oMLX](https://github.com/jundot/omlx?ref=loom.ogbuji.net), a native inference server for Apple Silicon with continuous batching and tiered KV caching. [I've long said MLX is the secret weapon of AI DIY](https://github.com/uogbuji/mlx-notes?ref=loom.ogbuji.net), and this article takes that argument into one more arena.

Secondly: the graph itself is [Onya](https://github.com/OoriData/Onya?ref=loom.ogbuji.net), a knowledge graph model and format I've been developing at Oori Data. The Gemini walkthrough ends with a networkx object and a pretty matplotlib figure—compute, render, discard. Onya is designed with the mindset that the graph is the durable artifact. Extraction results merge idempotently, persist to a store, and analytics computed in networkx can flow _back into the graph_ as first-class, typed assertions. "Onya", by the way, is from Igbo _ọ́nyà:_ web, snare, and by extension network; the expanded sense is _ọ́nyà úchè_ , a web of knowledge.

## The challenge

Given a long document—we'll use a full book from Project Gutenberg—and only a local model:

  1. Extract a knowledge graph of characters and relationships
  2. Do it within an honest local context window, not an 800k-token single request
  3. Keep the graph as a queryable, persistent, growable artifact
  4. Run real graph analytics, and keep _those results_ in the graph too



## Setup

I'll be presenting Python code, highly suggest that you're working in a virtual environment. Point an OpenAI client at your local server. With oMLX that looks like:

```python
from openai import OpenAI  # Must be installed: `pip install openai`

LLM_MODEL = 'mlx-community/Qwen3.6-35B-A3B-6bit'  # or whatever you've loaded
client = OpenAI(base_url='http://localhost:8000/v1', api_key='local')  # Use whatever port and key set when installing oMLX
```

A word on the model. Pulling _entities_ out of text is easy enough that a tiny 4B model does it well; pulling _relationships_ —the edges that make a graph a graph—turned out to want more heft. I say more about this in the "Cold Water" section below. So I've landed on Qwen 3.6 35B-A3B: a mixture-of-experts model with 35 billion parameters total but only about 3 billion _active_ per token, so it punches near a much larger model's weight while generating at small-model speed. At 6-bit it wants roughly 26GB of RAM, meaning you're looking at a 32GB Mac as the price of admission for relationship extraction that isn't a cloud call. If you're intrigued by this, check out [my article on Apple's MLX](https://huggingface.co/blog/ucheog/mlx-day-one?ref=loom.ogbuji.net). Smaller machine? A 4B model (`mlx-community/Qwen3.5-4B-8bit`, ~5GB) will still give you a decent entity graph; just don't expect it to wire the relationships together.

Install Onya in your venv, including the networkx extra (0.4.2 or later, for the sharpened parser errors the repair loop leans on):

```bash
pip install 'onya[nx]>=0.4.2' matplotlib
```

The core install is deliberately lean; networkx rides in an extra, is imported lazily, and matplotlib never becomes a dependency of Onya at all, though we'll add it for this article.

## Onya in about ninety seconds

Onya's conceptual model is small on purpose. A **node** has an IRI identifier, a set of types, and a set of assertions. An **assertion** is either a **property** (label IRI → string value) or an **edge** (label IRI → target node). Assertions can themselves carry assertions, so you can richly annotate relationships.

What makes it interesting for LLM work is the serialization, **Onya Literate** : a Markdown dialect. Here's a complete graph — the opening relationships of [Chinua Achebe's great novel, _Things Fall Apart_ ](https://en.wikipedia.org/wiki/Things_Fall_Apart?ref=loom.ogbuji.net):

```markdown
# @docheader

* @document: https://example.org/books/things-fall-apart
* @nodebase: https://example.org/books/things-fall-apart/
* @schema: https://schema.org/

# Okonkwo [Person]

* name: Okonkwo
* description: A renowned wrestler and self-made man of Umuofia
* children -> Nwoye
* children -> Ezinma
* homeLocation -> Umuofia

# Unoka [Person]

* name: Unoka
* description: A gentle flutist, and a debtor
* children -> Okonkwo

# Nwoye [Person]

* name: Nwoye

# Ezinma [Person]

* name: Ezinma

# Umuofia [Place]

* name: Umuofia
```

A `# @docheader` block sets the document IRI and the bases against which node ids, property labels, and types resolve; each `# NodeID [Type]` block is a node; `* label: value` is a property; `* label -> Target` is an edge. That's most of the format. It renders as perfectly reasonable Markdown on GitHub, diffs  
cleanly, and—the point of this article—it's a format a language model can very handily _write_. BTW if you're into putting Unicode to good use, you can replace those ASCII arrows, `->` with `→`.

![](https://storage.ghost.io/c/82/c0/82c0f4a1-bd31-487c-9c3e-cb9f780d0874/content/images/2026/07/tfa_web.png) Stylized representation of the Things Fall Apart graph snippet

Note: Yes, naming the parental relationship "children" feels itchy to my data architect bones, which would want a singular such as "child", but I am intentionally [sticking to schema.org](https://schema.org/children?ref=loom.ogbuji.net). Sometimes well-known and widely shared semantics hold the advantage over spotless ones.

## The output format is the game entire

Picard's article has an excellent section on output token economics: he moves from JSON to TSV tables and banks a 60–70% reduction in output tokens, which with LLMs is directly a speed and cost win. The insight is right, and locally it bites even harder; on your own hardware, output tokens are wall-clock time you personally sit through.

But TSV buys that efficiency by shattering the graph into two disconnected tables of integer ids, which somebody (you) must then reassemble. Onya Literate is my answer to the same pressure from a different direction: far leaner than JSON in any flavor—no braces, no quoted keys, values unquoted in the common case—while remaining self-describing, human-legible, and parseable directly into a real graph model, with no integer-id reassembly step lying in wait downstream. Measure it yourself against your model's own tokenizer:

```python
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained('mlx-community/Qwen3.6-35B-A3B-6bit')
for name, text in [('pretty JSON', pretty_json), ('compact JSON', compact_json),
                   ('TSV', tsv), ('Onya Literate', onya_text)]:
    print(f'{name:14} {len(tok.encode(text)):6,} tokens')
```

On the small graph above, rendered four ways, the Qwen 3.6 tokenizer gives me 418 tokens for pretty JSON, 224 for compact JSON, 96 for TSV, and 187 for Onya Literate. So Literate more than halves pretty JSON and slips under even compact JSON, while staying self-describing and diff-friendly. TSV is lighter still, but it gets there by melting every identifier down to a bare integer and dropping the document and base IRIs entirely, which is precisely the identity information you'll be reassembling by hand the moment you cut the document into chunks. Furthermore, 50 of Literate's 187 tokens here are the fixed docheader: a per-chunk cost that all but vanishes against a real 12k-token excerpt, so on production-sized chunks the gap over JSON only widens in Literate's favor. Note: The runnable measurement, plus all four serializations of this graph, lives beside this article as `measure_tokens.py` and `tfa-relationships.*`.

There's a second, sneakier advantage. Models have marinated in Markdown their entire training lives. Asking a local model to emit a rigid bespoke syntax is asking for trouble; asking it to write structured Markdown with a few conventions is playing to its strengths.

## Steering without a sampler

Readers of my [power steering piece](https://huggingface.co/blog/ucheog/llm-power-steering?ref=loom.ogbuji.net) know I'm an evangelist for schema-steered structured output (3SO)—constraining the sampler so structure is guaranteed rather than begged for. So let me be straight: Onya Literate isn't a JSON schema, and I'm not steering the sampler here._You could get a long way with a GBNF grammar for the Literate subset: a fun exercise I'll leave for you._

![](https://storage.ghost.io/c/82/c0/82c0f4a1-bd31-487c-9c3e-cb9f780d0874/content/images/2026/07/image-1.png) Illustration from the schema-steered structured output article

Instead I use the next best thing, which the format makes unusually practical: **validation by parse, with the parser's own errors as repair feedback**. Onya Literate is a real grammar, so the structurally broken output a model actually tends to produce fails to parse instead of slipping through as plausible nonsense. Common errors include code fences wrappers, prefacing with "Sure, here's the  
graph:", a property line adrift from any node block, a node identifier with a stray space or period. Onya 0.4.2's parser errors are written to support parse/error retry loops: they name the offending token and suggest a fix: _"a node identifier must be a single token with no spaces; got`Capt. Doran`. Use e.g. `CaptDoran`"_—so handing the exception straight back is usually enough for even a small model to correct itself on the next attempt:

I keep the prompts out of the code, in a [WordLoom](https://github.com/OoriData/WordLoom/?ref=loom.ogbuji.net) file, so I can review, diff, git commit and swap prompt variants as I refine them, without touching Python. I'll be writing more about Word Loom in future articles, but for now here is the file with prompts we'll be using:

```toml
# prompts/extract.loom.toml
lang = "en"

[kg-extract]
_m = ["doc_iri", "nodebase", "chunk"]
_ = """You are extracting a knowledge graph from a document excerpt, as Onya Literate (a Markdown format). Follow these rules exactly:

- Begin with this docheader, verbatim:

# @docheader

* @document: {doc_iri}
* @nodebase: {nodebase}
* @schema: https://schema.org/

- One heading block per distinct entity, in the form `# Identifier [Type]`, where Type is one of Person, Organization, Place. Concrete example: `# RobertKing [Person]`.
- The Identifier is a stable HumpCase rendering of the entity's fullest name in THIS excerpt, with no spaces or punctuation (Robert King -> RobertKing, Charming Sally -> CharmingSally). Do not write the literal words "Identifier" or "NodeId"; use the actual name. Reuse the same Identifier for the same entity everywhere it appears.
- `* name: <full name>` on every node. Add `* jobTitle:`, `* description:` when the text supports them.
- CRITICAL: capture relationships BETWEEN entities as edges, not just prose. Whenever the text says one person owns, serves, befriends, fathers, marries, or works for another, emit an edge: `* knows -> ThatPerson`, `* parent -> ThatPerson`, `* memberOf -> ThatOrg`. Prefer edges between two Person or Organization nodes; do not put a relationship only in a description. Every edge target must be a node block in your output.
- Nodes are NAMED individuals (Person), organizations (Organization), and places (Place) only. Skip ships, dates, and bare roles or common nouns (a slave, the master, the king), and ignore subscriber lists and tables of contents.
- Use only information from the excerpt. No preamble, no code fences: output raw Onya Literate only.

Excerpt:
{chunk}"""

[kg-repair]
_m = ["error"]
_ = """Your output failed to parse: {error}
Fix the problem and output the corrected, complete Onya Literate only."""
```

Notice this uses the [TOML format](https://toml.io/en/?ref=loom.ogbuji.net). A small loader reads those sections; the loop renders `kg-extract`, and on a parse failure feeds the exception through `kg-repair`:

```python
from onya.graph import graph
from onya.serial.literate import LiterateParser
import prompts   # small WordLoom loader; see the companion repo

def extract_chunk(chunk, doc_iri, nodebase, retries=2):
    '''One chunk -> one parsed Onya graph, with parse errors fed back for repair.'''
    prompt = str(prompts.load('extract.loom.toml', 'kg-extract').render(
        doc_iri=doc_iri, nodebase=nodebase, chunk=chunk))
    messages = [{'role': 'user', 'content': prompt}]
    for attempt in range(retries + 1):
        text = client.chat.completions.create(
            model=LLM_MODEL, messages=messages, temperature=0.0,
            # Reasoning models emit a "Thinking Process:" preamble that breaks the parse; turn it off so
            # the model writes raw Onya Literate. (oMLX and vLLM honor this; Ollama uses `think: false`.)
            extra_body={'chat_template_kwargs': {'enable_thinking': False}},
        ).choices[0].message.content
        g = graph()
        try:
            LiterateParser().parse(text, g)
            return g
        except Exception as e:  # noqa: BLE001 — parser errors vary; all are feedback
            repair = str(prompts.load('extract.loom.toml', 'kg-repair').render(error=str(e)))
            messages += [{'role': 'assistant', 'content': text}, {'role': 'user', 'content': repair}]
    raise RuntimeError('Chunk failed to parse after retries')
```

Not a guarantee, but in practice, with a capable local model at 0 temperature, most chunks parse on the first try, and nearly all survive one repair round. This is the pragmatic middle of the road between begging and steering.

## Chunking, and why merge semantics is the real story

Sometimes resource constraints clarify architecture more than they serve as a handicap. That's the case here with small/local LLMs. Picard's finale feeds all four volumes of _Le Comte de Monte-Cristo_ —840k tokens—to Gemini in one request. Glorious, but not available to us except on the cloud. A local model sees perhaps 32k tokens at a time, so we chunk up the content. This is where the integer-id tabular approach develops a serious problem: chunk 1's entity `0` and chunk 7's entity `0` are different people, and reconciling them is now a new weekend project.

Onya's answer is structural. Entity identity is an IRI, minted from the entity's name under a stable `@nodebase`, so `RobertKing` in chunk 3 and `RobertKing` in chunk 7 resolve to _the same node_ , by construction. Parsing multiple documents into one graph simply accumulates assertions as distinct occurrences; then `merge()`—an explicit, on-demand operation—collapses duplicates  
under the spec's identity rules. Extraction across chunks becomes idempotent graph union.

For our full-scale target I've chosen a book that completes this article's Igbo through-line: _The Interesting Narrative of the Life of Olaudah Equiano_ (1789), the memoir of the kidnapped Igbo child who bought his own freedom and became a founding voice of British abolitionism; the first great Igbo voice in English print. The text is comfortably in the public domain:

```python
import httpx

raw = httpx.get('https://www.gutenberg.org/cache/epub/15399/pg15399.txt').text
# Trim to the narrative proper: this 1789 edition opens with a title page, a long subscriber roll, and
# a table of contents, none of them story characters. Starting at chapter one keeps them out of the graph.
book = raw[raw.find('CHAPTER I.'):]
DOC_IRI = 'https://example.org/books/equiano-narrative'
NODEBASE = DOC_IRI + '/'

def chunks(text, size=12_000 * 4):  # ~12k tokens at ~4 chars/token; tune to your context
    for i in range(0, len(text), size):
        yield text[i:i + size]

g = graph()
for i, chunk in enumerate(chunks(book)):
    try:
        cg = extract_chunk(chunk, DOC_IRI, NODEBASE)
    except RuntimeError:
        continue   # a small model on a gnarly chunk can burn its retries; skip and press on
    g.union(cg)   # model-level union: rebinds targets, validates ids, accumulates occurrences
    print(f'chunk {i}: graph now {len(g)} nodes')
```

![](https://storage.ghost.io/c/82/c0/82c0f4a1-bd31-487c-9c3e-cb9f780d0874/content/images/2026/07/RR7BJ25EX5E6HFVPZLKCUK7L6I.png) Olaudah Equiano, 1745-1797

The aliasing problem—the one hard identity problem no system solves for free—is written into this book's very title: _Olaudah Equiano, or Gustavus Vassa_. The author spent much of his life under a name a slaver imposed on him, and chunks drawn from those years will mint a `GustavusVassa` node distinct from `OlaudahEquiano`. They land as separate nodes you reconcile with an `alias_of`-style edge in a later pass, LLM-assisted or by hand. Furthermore, because assertions can carry assertions, that reconciliation can itself be annotated with its provenance. The crux is that cross-chunk identity is a property of the data model, not a post-processing chore, and the residue it can't dissolve is exactly the residue that deserves this additional curation.

## Checkpoint it: the graph is a record, not just a printout

Onya has a pluggable persistence layer, and its correctness criterion is exactly the property we've just leaned on: a round trip through a store must be indistinguishable from an in-memory graph union. SQLite ships in the box, dependency-free, which suits the local ethos:

```python
from onya.store.sync import connect

with connect('sqlite:equiano.db') as store:
    store.put(DOC_IRI, g, merge=True)
```

`merge=True` means re-running extraction creates a union into what's already stored rather than clobbering it. When you outgrow the laptop there's a PostgreSQL backend (`onya[postgres]`), with the same merge semantics, of course.

## The round trip: analytics as first-class data

Now the showcase. Onya's `onya.serial.nx` is a projection into networkx, which instantly buys us every centrality measure, community detector, and layout algorithm that project has spent two decades accumulating. But the projection alone would just be catching up to where the Gemini article already stands. The difference is the trip _home_ :

```python
import networkx
from onya.serial import nx
from onya.terms import ONYA_INTERP

ANALYTICS = 'https://example.org/analytics/'

# The small model mis-typed a few ships and places as people (see "Cold Water"); drop them so the
# social graph reads cleanly. They stay in the stored graph — this is only a view for analysis.
NON_PERSON = {NODEBASE + n for n in ('CharmingSally', 'Carcass', 'RaceHorse', 'Jamaica', 'WesterHall')}

# Project. merge() first (above) for a normalized view; the projection is honest about the graph as-is.
mg = nx.to_networkx(g)
people = {str(n.id) for n in g.typematch('https://schema.org/Person')} - NON_PERSON
mg = mg.subgraph(people).copy()   # the @document node is a node too, but not a story character

# A memoir is an ego network: nearly everyone connects through the author, leaving one dense hub and a
# long tail of one-off mentions. Study the giant connected component, the people whose lives actually
# interlock, rather than that scatter.
giant = mg.subgraph(max(networkx.connected_components(mg.to_undirected()), key=len)).copy()

# Compute. Anything networkx offers.
betweenness = networkx.betweenness_centrality(giant)
communities = networkx.community.louvain_communities(giant.to_undirected(), seed=42)
community_of = {node: i for i, comm in enumerate(communities) for node in comm}

# Write back. Results become typed, merge-safe Onya assertions.
nx.write_back(g, ANALYTICS + 'betweenness', betweenness, interp=ONYA_INTERP('number'))
nx.write_back(g, ANALYTICS + 'community', community_of, interp=ONYA_INTERP('number'))

with connect('sqlite:equiano.db') as store:
    store.put(DOC_IRI, g, merge=True)
```

Equiano's own node tops every centrality measure—betweenness 0.81 against the next node's 0.15: normal for a memoir. The signal lies in what nodes cluster _around_ the hub. On my run, Louvain tweezered four communities out of the giant component, and the largest few are recognizably the circles of a life: the Montserrat trading world of Robert King (with the merchant captains Doran and Farmer, and Nancy), the officers of the 1773 Phipps expedition toward the North Pole (Phipps and Lutwidge), and the knot of names around the London kidnapping of his friend John Annis. Staring out of the graph, two nodes, `Gustavus Vassa` and `Equiano`, for one man. This is the aliasing problem I mentioned.

This is the step I most wanted to add to the workflow Picard sketched. The centrality scores aren't only in a matplotlib figure that evaporates when the notebook dies; they're properties in the graph, each carrying a _data contract_ : that `interp=ONYA_INTERP('number')` records, on the assertion itself, that this string is to be read as a number. Onya's core stays honestly string-valued; contracts are  
honored at boundaries you choose, never implicitly. `replace=True` by default means re-running analytics after the graph grows is idempotent. The results are immediately queryable through the graph's own selector:

```python
from onya.interp import value_of

top = sorted(g.select(label=ANALYTICS + 'betweenness'),
             key=value_of, reverse=True)[:5]
for p in top:
    print(f'{value_of(p):.4f}  {p.origin.id}')
```

It's valuable for long-running analysis to have a graph which serves as a durable system of record, through different type an utility projections, across workflows, with clear semantics rather than potentially disconnected id tables. Visualizations are just utility outputs, subservient to the data.

## Seeing it

Rendering is deliberately _not_ Onya's job, but from the networkx projection it's a short walk, and we can even size and color from values stored in the graph itself:

```bash
pip install 'onya[nx]>=0.4.2' matplotlib
```0

![](https://storage.ghost.io/c/82/c0/82c0f4a1-bd31-487c-9c3e-cb9f780d0874/content/images/2026/07/equiano_kg.png) Gustavus Vassa the central hub, Robert King's Montserrat circle branching off (Equiano, Nancy, Doran, Farmer), the John Annis and Phipps-expedition clusters in their own colors, and the separate `Equiano` node that betrays the aliasing

For a quick structural look without the matplotlib layer, Onya's CLI exports Mermaid or Graphviz DOT directly from a Literate file: `onya convert equiano.onya.md > out.mmd`, paste into [mermaid.live](https://mermaid.live/?ref=loom.ogbuji.net)…done.

## Cold Water

A few honest addenda.

  * The parse-and-repair loop is a statistical comfort, without the guarantee that true sampler-steered output gives you; a small enough model on a gnarly enough chunk will occasionally burn your retry budget. On my run two of ten chunks skipped that way, and the pipeline was built to shrug and press on rather than die.
  * Extraction _quality_ is a property of the model, and it degrades ungracefully as you shrink. A 4B model gave me clean entities but essentially no edges; the 35B-A3B wired the relationships together but still, here and there, typed a ship (`Charming Sally`) or a place (`Jamaica`) as a Person, and split one man across `Gustavus Vassa`, `Equiano`, and `Olaudah`. Smaller local models are also prompt-_fragile_ : the same prompt that behaves on one chunk can send them into a repetition loop on the next. I filtered the mis-typed handful out of the figure by name; a shippable pipeline would want a validation pass, rather than a hand-scribbled list.
    * If you want to measure this trade-off across models yourself, the `model_assessment/` directory in this article's code bundle scores a given model on wall-clock, skipped chunks, and how many known relationships it recovers. And if you want to dig more obsessively into what I found doing exactly that, kept a hard-bitten lab notebook: Field notes: baking off local LLMs for knowledge-graph extraction. Tidbits such as how speculative decoding torpedoed one MoE, why Gemma and Qwen fail differently, and why most prompt tweaks made things worse.
  * The networkx projection is deliberately lossy in this first version: first-level structure only; nested assertion metadata and identified-assertion edge targets stay behind in the Onya graph (which, note, is precisely a loss the _writeback_ never suffers, since `write_back` operates on the full model).
  * LLM extraction itself has all the usual caveats about implied entities, memorized-versus-extracted knowledge, and aliasing that Picard covers well and I won't rehash.

![](https://storage.ghost.io/c/82/c0/82c0f4a1-bd31-487c-9c3e-cb9f780d0874/content/images/2026/07/Racehorse-progress-detail-14.10.17-IMG_15831-1.jpg) [Detail from "Racehorse progress", a painting by Gordon Frickers](https://frickers.co.uk/art/blog/2017/10/16/olaudah-equiano-i-salute-you/?ref=loom.ogbuji.net), inspired by the life and journeys of Olaudah Equiano

## Sail away!

The pattern, in a trice:

  * prompt a local model to emit Onya Literate
  * validate by parsing, repairing with the parser's own errors
  * chunk long documents and let IRI identity plus explicit `merge()` make extraction an idempotent union
  * checkpoint to a store; project to networkx for the heavy analytical  
lifting
  * write the results back as typed assertions, so the analysis is part of the record. 



Every piece runs on hardware you own, against any OpenAI-compatible endpoint.

Onya is young and moving fast, though it builds on a quarter-century heritage, though Versa and RDF. Feedback, issues, and battle scars from real-world use are very welcome [on GitHub](https://github.com/OoriData/Onya?ref=loom.ogbuji.net). If you try this with your own local stack, I'd love to hear what worked well, and what held you in a headlock.

_Thanks to Laurent Picard, whose Gemini article prompted this response in the best sense of the word. It also inspired me to adds the`onya.serial.nx` capability in Onya 0.4.1._

[ ](/arsenal-champions/)

### Published by:

[ ![Uche Ogbuji](https://storage.ghost.io/c/82/c0/82c0f4a1-bd31-487c-9c3e-cb9f780d0874/content/images/size/w150/2022/08/IMG_20200215_193319.jpg) ](/author/uche/ "Uche Ogbuji")

### You might also like...

May 08 

## A literal out of body experience; Nigerian Modernism at the Tate Modern [Áhị́rị́]

15 min read [ ](/nigerian-modernism-tate-modern-ahiri/) Oct 27 

## Mushroom talk [Ókwú éló]

6 min read [ ](/mushroom-talk/) Sep 04 

## Fourthought…Kadomo/Zepheira…Oori! [Àzụ́m áhị́á]

8 min read [ ](/azum-ahia/) Jul 23 

## Juju na lie [Ọ́gwụ̀ bụ àsị́]

6 min read [ ](/juju-na-lie/) Jun 25 

## Sun on a rocket [Anyanwu nọ n'égbè]

8 min read [ ](/sun-on-a-rocket/) Loomiverse © 2026 

  * Sign up

[Powered by Ghost](https://ghost.org/)
