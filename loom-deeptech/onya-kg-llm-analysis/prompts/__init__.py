'''WordLoom prompt loading for the extraction pipeline.

Prompts live in loom TOML files beside this module (`prompts/*.loom.toml`), never inline in Python —
so they can be reviewed, diffed, and swapped without touching code, and prompt experiments can be kept
as separate files on disk. See https://github.com/OoriData/WordLoom/.

    from prompts import load
    text = str(load('extract.loom.toml', 'kg-extract').render(doc_iri=..., nodebase=..., chunk=...))
'''
from functools import lru_cache
from pathlib import Path

import wordloom

HERE = Path(__file__).resolve().parent   # the prompts/ directory


@lru_cache(maxsize=16)
def _load(path_str, _mtime_ns):
    # cache keyed on (path, mtime) so edits during a session are picked up without a restart
    return wordloom.load(Path(path_str), lang='en', features={'file-inclusion'}, base_dir=HERE.parent)


def load(loom_file, key):
    '''Return a WordLoom language_item for `key` in `loom_file` (a name under prompts/).

    Call `.render(**kw)` then `str(...)` at the call site; don't thread the item through transport code.
    '''
    p = (HERE / loom_file).resolve()
    items = _load(str(p), p.stat().st_mtime_ns)
    if key not in items:
        avail = sorted(k for k, v in items.items() if k != str(v))  # section names only, not bodies
        raise KeyError(f'{key!r} not found in {loom_file}. Available: {avail}')
    return items[key]
