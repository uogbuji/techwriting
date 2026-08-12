#!/usr/bin/env python
'''Measure output-token cost of the same knowledge graph across four serializations.

The graph is the opening relationships of Chinua Achebe's *Things Fall Apart*, rendered as:
  - pretty JSON        tfa-relationships.pretty.json
  - compact JSON       tfa-relationships.compact.json
  - TSV (two tables)   tfa-relationships.tsv
  - Onya Literate      tfa-relationships.onya.md

All four encode identical facts, so token counts are a fair apples-to-apples comparison of
format overhead. Output tokens are what the model must *emit* during extraction, which locally
is wall-clock time you personally sit through.

Usage:
    pip install transformers
    python measure_tokens.py                            # default: mlx-community/Qwen3.6-35B-A3B-6bit
    python measure_tokens.py Qwen/Qwen3.5-4B            # measure against a different tokenizer
'''
import sys
from pathlib import Path

from transformers import AutoTokenizer

HERE = Path(__file__).parent
# Token counts are near-identical across the Qwen family; any Qwen tokenizer gives essentially these
# numbers. This is the model the article extracts with.
DEFAULT_MODEL = 'mlx-community/Qwen3.6-35B-A3B-6bit'

# (label, filename) — order controls display order
REPRESENTATIONS = [
    ('pretty JSON',   'tfa-relationships.pretty.json'),
    ('compact JSON',  'tfa-relationships.compact.json'),
    ('TSV',           'tfa-relationships.tsv'),
    ('Onya Literate', 'tfa-relationships.onya.md'),
]


def main(model_id=DEFAULT_MODEL):
    tok = AutoTokenizer.from_pretrained(model_id)
    samples = [(name, (HERE / fn).read_text()) for name, fn in REPRESENTATIONS]

    counts = {name: len(tok.encode(text)) for name, text in samples}
    baseline = counts['pretty JSON']  # the verbose starting point everyone reaches for first

    print(f'Tokenizer: {model_id}\n')
    print(f'{"format":14} {"chars":>7} {"tokens":>8} {"vs pretty JSON":>16}')
    print('-' * 48)
    for name, text in samples:
        n = counts[name]
        delta = '' if name == 'pretty JSON' else f'-{100 * (1 - n / baseline):.0f}%'
        print(f'{name:14} {len(text):7,} {n:8,} {delta:>16}')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MODEL)
