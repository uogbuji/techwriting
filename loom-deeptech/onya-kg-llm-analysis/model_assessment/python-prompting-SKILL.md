---
name: python-prompting
description: Prompt management for Python LLM/AI applications using WordLoom — declarative prompt/code separation, file layout, the shared loader pattern, file-inclusion (file:/glob:/dir:), naming conventions, and testing. Use when writing or refactoring prompts that get sent to Claude, OpenAI, OpenRouter, or any other LLM API from Python.
---

# Python Prompting (WordLoom)

## Purpose
All LLM prompts — system, user, repair, evaluation — live in [WordLoom](https://github.com/OoriData/WordLoom/) TOML files, never as inline Python string constants. Prompts are content, not code; treating them as content lets non-engineers review them, lets you version and diff them, and lets you swap them without reinstalling the package. This is the Oori standard for declarative prompt/code separation.

This skill complements [python-backend](../python/SKILL.md) — follow that one for Python coding conventions in tandem.

## Default rules

- **No inline prompts.** Never put a multi-line prompt in a Python `'''...'''` constant or as a default function argument. Move it to a `.loom.toml` file.
- **One shared loader module per project.** Don't reinvent loading in each feature module. Centralize in something like `pylib/prompts.py`.
- **One loom file per feature area**, under `prompts/` at the project root. Group sections that share file-included assets together.
- **Use WordLoom's file-inclusion** ([`file:` / `glob:` / `dir:` metadata values](https://github.com/OoriData/WordLoom/blob/main/implementation.md#extension-file-inclusion)) to compose prompts from external assets — schemas, examples, corpora — instead of pasting them into TOML.
- **Lexical path resolution only.** Never use `Path.exists()` in the loader — test patches like `with patch('pathlib.Path.exists', return_value=True)` will corrupt resolution. Decide bare-filename vs. absolute vs. relative from the path *shape*, not from filesystem state.
- **Anchor file-inclusion at the project root** by passing `base_dir=project_root` to `wordloom.load`. This lets a loom file under `prompts/` reach `data/`, `docs/`, etc. via uniform paths.
- **Cache by `(path, mtime)`**, so prompt edits during dev sessions are picked up without restarting.

## File layout

```
project_root/
├── prompts/
│   ├── feature_a.loom.toml
│   ├── feature_b.loom.toml
│   ├── shared_asset.md           # referenced from loom files via file:
│   └── example_outputs.md        # ditto
├── data/
│   └── kg/*.onya.md              # generated content; referenced via glob:
└── pylib/
    └── prompts.py                # shared loader
```

WordLoom's `file:` and `dir:` extensions enforce no-`..`-traversal: paths must be under `base_dir`. With `base_dir = project_root`, every path under the repo is reachable.

## Section naming conventions

| Suffix | Use for |
|---|---|
| `<feature>-sysprompt` | The system-role message |
| `<feature>-userprompt` | A templated user-role message |
| `<feature>` (no suffix) | The main user-role prompt when there's only one |
| `<feature>-<variant>` | Variants like `repair`, `summary`, `select` |
| `<feature>-<variant>-sysprompt` | Variant's own system message |

Example for a KG-construction feature:
```
[kg-summarize-sysprompt]      # system prompt for the main call
[kg-summarize]                # user prompt (the meaty one with {placeholders})
[kg-repair-sysprompt]         # system prompt for the repair pass
[kg-repair]                   # user prompt for the repair pass
```

## File-inclusion conventions

- **`file:relative/path.md`** — single file. Use for stable schemas, examples, reference docs.
- **`glob:pattern/*.ext`** — concatenation of files. Use for corpora and dynamic collections (each file is delimited with `=== filename ===` in the rendered output).
- **`dir:relative/path/`** — entire directory tree. Less common.

All paths are relative to `base_dir`. Include the directory in the path (`file:prompts/foo.md`, not `file:foo.md`) when `base_dir=project_root`.

## The shared loader

A minimal but complete loader. Adapt the module name and env-var prefix to the project.

```python
'''Centralized WordLoom prompt loading.

All prompts live in ``prompts/*.loom.toml`` at the project root. Each loom file
groups prompts by feature area; file-inclusion is always enabled with
``base_dir`` anchored at the project root.
'''

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path
from typing import Any

import wordloom

PROMPTS_DIR_ENV = 'MYAPP_PROMPTS_DIR'   # rename per project
ROOT_ENV        = 'MYAPP_ROOT'          # rename per project
DEFAULT_DIRNAME = 'prompts'


def project_root() -> Path:
    env = os.environ.get(ROOT_ENV)
    return Path(env).resolve() if env else Path.cwd().resolve()


def prompts_dir() -> Path:
    env = os.environ.get(PROMPTS_DIR_ENV)
    return Path(env).resolve() if env else project_root() / DEFAULT_DIRNAME


def _resolve(loom_path: str | Path) -> tuple[Path, Path]:
    '''Lexical resolution — no filesystem checks. Returns (abs_path, base_dir).'''
    p = Path(loom_path)
    if p.is_absolute():
        abs_path = p.resolve()
        return abs_path, abs_path.parent
    if len(p.parts) == 1:                  # bare filename
        return (prompts_dir() / p).resolve(), project_root()
    abs_path = p.resolve()                 # multi-segment relative
    return abs_path, abs_path.parent


@lru_cache(maxsize=16)
def _cached_load(path_str: str, mtime_ns: int, base_dir_str: str) -> dict[str, Any]:
    return wordloom.load(
        Path(path_str), lang='en', features={'file-inclusion'},
        base_dir=Path(base_dir_str),
    )


def load_file(loom_path, *, base_dir=None) -> dict[str, Any]:
    abs_path, default_base = _resolve(loom_path)
    bdir = Path(base_dir).resolve() if base_dir else default_base
    return _cached_load(str(abs_path), abs_path.stat().st_mtime_ns, str(bdir))


def _section_keys(items: dict[str, Any]) -> list[str]:
    '''WordLoom indexes each item twice (by section name AND by body text).
    Surface only the section names in error messages.'''
    return sorted(k for k, v in items.items() if k != str(v))


def load(loom_path, key: str, *, base_dir=None) -> wordloom.language_item:
    items = load_file(loom_path, base_dir=base_dir)
    if key not in items:
        raise KeyError(
            f'WordLoom key {key!r} not found in {loom_path!s}. '
            f'Available: {_section_keys(items)}'
        )
    return items[key]


def try_load(loom_path, key, *, base_dir=None):
    try:
        return load(loom_path, key, base_dir=base_dir)
    except KeyError:
        return None


def clear_cache() -> None:
    _cached_load.cache_clear()
```

Why `_section_keys`? WordLoom indexes each `[section]` *twice* — once by the section name, once by the body text — so a naive `list(items)` will drown a `KeyError` message in thousand-character prompt bodies. The `k != str(v)` filter keeps only section names.

## Caller pattern

```python
from myapp import prompts

# In a call site:
sysprompt = str(prompts.load('kg.loom.toml', 'kg-summarize-sysprompt').render()).strip()
user_prompt = prompts.load('kg.loom.toml', 'kg-summarize').render(
    master_doc=md,
    node_link=link,
    node_name=name,
)
```

Pass rendered strings to the HTTP layer; never thread `language_item` objects through generic transport functions. That keeps the prompt boundary tight: render at the edge, send strings to the API.

## Before / after — inline → loom

```diff
-    system = (
-        'You are a RevOps assistant. Summarize sales calls in clear markdown. '
-        'Use ## headings: Overview, Key points, Action items, Risks, Next steps. ...'
-    )
-    user = f'## Meeting: {title}\n\n{text}'
+    system = str(prompts.load(INGEST_LOOM, 'meeting-summary-sysprompt').render()).strip()
+    user   = prompts.load(INGEST_LOOM, 'meeting-summary-userprompt').render(
+        title=title, transcript=text,
+    )
```

## What NOT to do

- `system = 'You are a helpful assistant. ...'` inline in Python.
- `system_prompt: str = DEFAULT_SYSTEM_PROMPT` as a function default (defaults rot; loom files don't).
- Module-level `_LOOM_CACHE = None` + `_load_loom()` per feature. Use the shared loader.
- `Path.cwd() / 'prompts.loom.toml'` — too brittle for cron/systemd; use env var + `prompts_dir()`.
- Putting prompt content into `src/utils/`, `lib/prompts/`, etc. as Python modules. Prompts are content, not code.
- Adding `..` to a `file:` path to escape `prompts/`. Re-anchor `base_dir` at project root and use full paths instead.

## Testing

- Fixtures write a loom file into `tmp_path`. Tests pass it as an **absolute path** to the loader — `_resolve`'s "absolute → use as given" branch handles this correctly.
- Always call `prompts.clear_cache()` in fixtures that rewrite loom files (or use a fresh `tmp_path` per test).
- Test the loader's resolution rules separately from the consumer tests. Cover: bare filename, absolute path, multi-segment relative, missing-key error, `try_load` for optional keys.
- Avoid `patch('pathlib.Path.exists', return_value=True)` style monkey-patches around code that calls the loader — they'll corrupt resolution. If a test needs to fake the existence of *application* files, narrow the patch scope (use a context manager that only wraps the relevant call).

## When NOT to use WordLoom

- **One-line fixed strings** that act as boilerplate rather than prompts (e.g., `'Respond in JSON only.'` appended to user content). Inline is fine.
- **Throwaway scripts** in `scratch/` or notebooks.
- **Prototype phase** where the prompt is still being explored interactively — but move to loom before the code lands on `main`.

## Migration heuristics

When refactoring a project that has inline prompts:

1. Grep for `'You are'`, `'system ='`, multi-line `'''...'''` blocks near `httpx.post`, `client.messages.create`, etc.
2. For each hit, identify which feature owns it and which loom file it should land in.
3. Move the body verbatim into a `[section]` entry; convert Python `{var}` interpolations to WordLoom `{var}` placeholders, listing them in `_m = [...]`.
4. Replace the inline string with a `prompts.load(...).render(...)` call at the same site.
5. Add a test that loads the prompt and verifies it renders without `KeyError`.

## If the task is unclear

Ask which LLM provider/SDK the project targets (Anthropic, OpenAI, OpenRouter, etc.), whether prompts must be hot-editable in production (affects whether they're packaged or kept at repo root), and whether there are existing conventions for `prompts/` placement.

{{skill_snippet}}
