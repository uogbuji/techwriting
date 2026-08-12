**Companion code to "[Building and working knowledge graphs with Onya and LLMs](https://loom.ogbuji.net/tech/building-and-working-knowledge-graphs-with-onya-and-local-llms/)"**

Runnable, woven-together versions of the code fragments in the article. The in-article snippets are kept
deliberately short; these files fill in the plumbing for anyone who wants to replicate the whole thing.

## Files

| File | Article section | What it does |
|------|-----------------|--------------|
| `measure_tokens.py` | *Why the output format is the whole ballgame* | Tokenizes the same graph in four serializations and prints the comparison. |
| `tfa-relationships.onya.md` | *Onya in about ninety seconds* | The Things Fall Apart example graph — the source of truth for the four renderings. |
| `tfa-relationships.pretty.json` / `.compact.json` / `.tsv` | *Why the output format…* | The same graph as pretty JSON, compact JSON, and Picard-style two-table TSV. Hand-authored to encode identical facts, for a fair token comparison. |
| `equiano_extract.py` | *Setup* → *Checkpoint it* | Fetch the book, chunk it, prompt a local model for Onya Literate, validate-by-parse with repair, union into one graph, checkpoint to `equiano.db`. **Needs a local LLM server.** |
| `prompts/extract.loom.toml` | *Steering without a sampler* | The extraction + repair prompts, as a [WordLoom](https://github.com/OoriData/WordLoom/) file (loaded by `prompts/__init__.py`) rather than inline in Python. |
| `equiano_analyze.py` | *The round trip* → *Seeing it* | Load `equiano.db`, project to networkx, compute betweenness + communities, write them back as typed assertions, query, and render `equiano_kg.png`. No LLM needed. |

## Setup

```sh
pip install 'onya[nx]>=0.4.2' openai httpx matplotlib transformers wordloom
```

`equiano_extract.py` needs a local OpenAI-compatible server (oMLX, llama.cpp, vLLM, LM Studio, Ollama, …)
serving a capable model. Point it there via environment variables:

```sh
export ONYA_LLM_BASE_URL=http://localhost:8000/v1
export ONYA_LLM_KEY=local
export ONYA_LLM_MODEL=mlx-community/Qwen3.6-35B-A3B-6bit
```

## Run

```sh
python measure_tokens.py                 # token economics (standalone; no LLM, no db)
python equiano_extract.py --limit 2      # quick smoke test: first 2 chunks
python equiano_extract.py                # full extraction -> equiano.db + equiano.onya.md
python equiano_analyze.py                # analytics + writeback + equiano_kg.png
onya convert equiano.onya.md > equiano.mmd   # quick Mermaid export; paste into mermaid.live
```
