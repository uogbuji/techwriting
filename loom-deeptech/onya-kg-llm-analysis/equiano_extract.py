#!/usr/bin/env python
'''Extract a knowledge graph from a long public-domain book with a *local* LLM.

Companion code for "Building and working knowledge graphs with Onya and LLMs". This is the woven,
runnable version of the fragments in the "Setup", "Steering without a sampler", "Chunking", and
"Checkpoint it" sections: fetch the book, chunk it to a local context window, prompt a local model to
emit Onya Literate, validate each chunk by parsing (feeding the parser's own errors back for repair),
union the chunks into one graph under stable IRI identity, and checkpoint to a SQLite store.

The companion script `equiano_analyze.py` picks up from the store this script writes.

The extraction prompts live in `prompts/extract.loom.toml` (a WordLoom file), not inline in this code —
so they can be reviewed, diffed, and swapped without editing Python. See https://github.com/OoriData/WordLoom/.

Prerequisites:
    pip install 'onya[nx]>=0.4.2' openai httpx wordloom
    # ...and a local OpenAI-compatible server (oMLX, llama.cpp, vLLM, LM Studio, Ollama, ...) serving a
    # capable model. Point the env vars below at it.

Usage:
    ONYA_LLM_MODEL=mlx-community/Qwen3.6-35B-A3B-6bit python equiano_extract.py
    python equiano_extract.py --limit 2      # only the first 2 chunks, for a quick smoke test
'''
import argparse
import os

import httpx
from openai import OpenAI

from onya.graph import graph
from onya.serial import literate
from onya.serial.literate import LiterateParser
from onya.store.sync import connect

import prompts   # local WordLoom loader (prompts/__init__.py)

# --- Local model behind a plain OpenAI-compatible endpoint. Override via environment. ---
LLM_MODEL = os.environ.get('ONYA_LLM_MODEL', 'mlx-community/Qwen3.6-35B-A3B-6bit')
client = OpenAI(
    base_url=os.environ.get('ONYA_LLM_BASE_URL', 'http://localhost:8000/v1'),
    api_key=os.environ.get('ONYA_LLM_KEY', 'local'),
)

# *The Interesting Narrative of the Life of Olaudah Equiano* (1789), public domain, Project Gutenberg.
BOOK_URL = 'https://www.gutenberg.org/cache/epub/15399/pg15399.txt'
DOC_IRI = 'https://example.org/books/equiano-narrative'
NODEBASE = DOC_IRI + '/'
STORE_URL = 'sqlite:equiano.db'
LITERATE_OUT = 'equiano.onya.md'

PROMPTS = 'extract.loom.toml'   # WordLoom file under prompts/


def extract_chunk(chunk, doc_iri, nodebase, retries=2):
    '''One chunk -> one parsed Onya graph, with parse errors fed back for repair.'''
    prompt = str(prompts.load(PROMPTS, 'kg-extract').render(
        doc_iri=doc_iri, nodebase=nodebase, chunk=chunk))
    messages = [{'role': 'user', 'content': prompt}]
    for attempt in range(retries + 1):
        text = client.chat.completions.create(
            model=LLM_MODEL, messages=messages, temperature=0.0, max_tokens=8000,
            # Qwen 3.5/3.6 and friends are reasoning models by default: they emit a "Thinking Process:"
            # preamble that both slows generation and breaks the parse. Turn thinking off so the model
            # emits raw Onya Literate. (This chat_template_kwargs form is honored by oMLX/vLLM; other
            # backends have their own switch — e.g. Ollama's `think: false`.)
            extra_body={'chat_template_kwargs': {'enable_thinking': False}},
        ).choices[0].message.content
        g = graph()
        try:
            LiterateParser().parse(text, g)
            return g
        except Exception as e:  # noqa: BLE001 — parser errors vary; all are feedback
            # Onya 0.4.2's LiterateSyntaxError messages are specific and actionable — they name the
            # offending token and the fix (e.g. "got `Capt. Doran`; use `CaptDoran`") — so the exception
            # fed straight back (via the kg-repair prompt) is enough for even a small model to self-correct.
            repair = str(prompts.load(PROMPTS, 'kg-repair').render(error=str(e)))
            messages += [{'role': 'assistant', 'content': text},
                         {'role': 'user', 'content': repair}]
    raise RuntimeError('Chunk failed to parse after retries')


def strip_gutenberg(text):
    '''Drop the Project Gutenberg header/license boilerplate so it doesn't pollute extraction.'''
    start = text.find('*** START OF')
    end = text.find('*** END OF')
    if start != -1:
        text = text[text.find('\n', start) + 1:]
    if end != -1:
        text = text[:text.rfind('*** END OF', 0, end + 1) if end != -1 else None]
    return text.strip()


def trim_front_matter(text, marker='CHAPTER I.'):
    '''Skip the book's own front matter — Equiano's 1789 edition opens with a title page, a long
    subscriber roll, and a table of contents, none of which are narrative characters. Start at the
    first chapter so the model isn't tempted to mint a node per subscriber.'''
    i = text.find(marker)
    return text[i:] if i != -1 else text


def chunks(text, size=12_000 * 4):  # ~12k tokens at ~4 chars/token; tune to your context window
    for i in range(0, len(text), size):
        yield text[i:i + size]


def checkpoint(g):
    '''Persist the whole graph. merge=True unions into what's stored rather than clobbering it, so
    re-running extraction (a revised chunking, a second volume, a resumed run) is idempotent union.'''
    with connect(STORE_URL) as store:
        store.put(DOC_IRI, g, merge=True)
    with open(LITERATE_OUT, 'w') as fp:
        literate.write(g, fp, document=DOC_IRI, nodebase=NODEBASE, schema='https://schema.org/')


def main(limit=None):
    book = trim_front_matter(strip_gutenberg(httpx.get(BOOK_URL, timeout=60, follow_redirects=True).text))
    total = (len(book) + (12_000 * 4) - 1) // (12_000 * 4)
    print(f'Book: {len(book):,} chars -> {total} chunks', flush=True)

    g = graph()
    for i, chunk in enumerate(chunks(book)):
        if limit is not None and i >= limit:
            print(f'Stopping at chunk limit {limit}', flush=True)
            break
        try:
            cg = extract_chunk(chunk, DOC_IRI, NODEBASE)
        except RuntimeError as e:
            # A chunk that never parses shouldn't sink the whole run — log and press on.
            print(f'chunk {i}/{total}: SKIPPED ({e})', flush=True)
            continue
        g.union(cg)   # model-level union: rebinds targets, validates ids, accumulates occurrences
        checkpoint(g)   # incremental: partial progress survives a crash or an interrupted run
        print(f'chunk {i}/{total}: graph now {len(g)} nodes (checkpointed)', flush=True)

    g.merge()   # explicit, on-demand: collapse duplicate assertions under the spec's identity rules
    checkpoint(g)
    print(f'Done. {len(g)} nodes checkpointed to {STORE_URL} and {LITERATE_OUT}', flush=True)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--limit', type=int, default=None, help='max chunks (smoke test)')
    main(**vars(ap.parse_args()))
