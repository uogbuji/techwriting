#!/usr/bin/env python
'''Download and pre-process *The Interesting Narrative of the Life of Olaudah Equiano* (1789) into a
clean plain-text file the assessment harness (and the article) can reuse without re-fetching.

Preprocessing:
  - strip the Project Gutenberg license header/footer
  - trim the book's own front matter (title page, subscriber roll, table of contents) so extraction
    isn't polluted by hundreds of subscriber names; the narrative proper starts at "CHAPTER I."

Output: equiano_narrative.txt (beside this script).

Usage:
    pip install httpx
    python fetch_equiano.py
'''
from pathlib import Path

import httpx

BOOK_URL = 'https://www.gutenberg.org/cache/epub/15399/pg15399.txt'
OUT = Path(__file__).parent / 'equiano_narrative.txt'


def strip_gutenberg(text):
    start = text.find('*** START OF')
    end = text.find('*** END OF')
    if start != -1:
        text = text[text.find('\n', start) + 1:]
    if end != -1:
        text = text[:text.rfind('*** END OF', 0, end + 1)]
    return text.strip()


def trim_front_matter(text, marker='CHAPTER I.'):
    i = text.find(marker)
    return text[i:] if i != -1 else text


def main():
    raw = httpx.get(BOOK_URL, timeout=60, follow_redirects=True).text
    book = trim_front_matter(strip_gutenberg(raw))
    OUT.write_text(book)
    print(f'Wrote {OUT} — {len(book):,} chars (~{len(book) // (12_000 * 4) + 1} chunks at 12k tokens)')


if __name__ == '__main__':
    main()
