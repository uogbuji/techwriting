'''Hand-curated ground truth for scoring extraction quality against *The Interesting Narrative of the
Life of Olaudah Equiano*.

This is a NON-EXHAUSTIVE sample of well-attested human-to-human relationships in the book. The harness
scores RECALL: of these known relationships, how many does a model's graph actually connect with an
edge? Recall is the honest, comparable metric here — full precision would require hand-labelling every
edge a model emits, which defeats the purpose of a quick model bake-off.

Matching is deliberately lenient and alias-aware, because the whole difficulty of this task is that
models name the same person many ways (Olaudah Equiano / Gustavus Vassa / Equiano) and hang titles on
them (Capt. Pascal / Michael Henry Pascal). Each entity below lists name variants; a graph node matches
an entity when, after lower-casing, stripping punctuation and dropping honorifics, the alias's tokens are
a subset of the node's tokens (so the single token "pascal" matches a "Michael Henry Pascal" node). A
relationship counts as recalled if ANY node matching entity A shares an edge (either direction, any
label) with ANY node matching entity B.
'''

# entity key -> set of name variants a model might plausibly emit
ENTITIES = {
    'equiano':        {'olaudah equiano', 'gustavus vassa', 'equiano', 'olaudah', 'vassa'},
    'pascal':         {'michael henry pascal', 'henry pascal', 'pascal'},
    'robert_king':    {'robert king'},
    'richard_baker':  {'richard baker', 'dick baker'},
    'daniel_queen':   {'daniel queen'},
    'guerin':         {'miss guerins', 'miss guerin', 'mary guerin', 'guerins'},
    'thomas_farmer':  {'thomas farmer', 'farmer'},
    'charles_irving': {'charles irving', 'doctor irving', 'irving'},
    'phipps':         {'john constantine phipps', 'constantine phipps', 'phipps', 'mulgrave'},
    'lutwidge':       {'skeffington lutwidge', 'lutwidge'},
    'granville_sharp': {'granville sharp', 'grenville sharp'},
    'john_annis':     {'john annis', 'annis'},
    'thomas_clarkson': {'thomas clarkson', 'clarkson'},
    'doran':          {'captain doran', 'doran'},
}

# (entity_a, entity_b, note) — well-attested relationships. Scored on edge existence, either direction.
RELATIONSHIPS = [
    ('equiano', 'pascal',          'Pascal bought Equiano, renamed him Gustavus Vassa, took him to sea'),
    ('equiano', 'robert_king',     'King bought Equiano; Equiano later bought his freedom from him'),
    ('equiano', 'richard_baker',   'shipboard companion and close friend'),
    ('equiano', 'daniel_queen',    'Queen taught Equiano to read, shave and dress hair aboard the Aetna'),
    ('equiano', 'guerin',          "Pascal's cousins; had Equiano baptised and showed him kindness"),
    ('equiano', 'thomas_farmer',   'Equiano sailed under Farmer, a trading captain for King'),
    ('equiano', 'charles_irving',  'joined Irving on the Arctic voyage and the Mosquito Coast plantation'),
    ('equiano', 'phipps',          'joined Phipps 1773 expedition toward the North Pole'),
    ('equiano', 'granville_sharp', 'appealed to Sharp over the John Annis case and the Zong massacre'),
    ('equiano', 'john_annis',      "friend kidnapped back into slavery; Equiano sought Sharp's help"),
    ('equiano', 'thomas_clarkson', 'fellow abolitionist'),
    ('equiano', 'doran',           'Captain Doran carried Equiano to Montserrat and sold him to King'),
    ('robert_king', 'thomas_farmer', 'King employed Farmer as a vessel captain'),
    ('phipps', 'lutwidge',         'Lutwidge commanded the Carcass alongside Phipps’s Racehorse'),
]

# The memoirist narrates in the first person, so he is "present" from the very first line even though
# his name string ("Gustavus Vassa") isn't printed until Pascal assigns it well into the book, and
# "Olaudah"/"Equiano" don't appear in the narrative body at all (they live in the trimmed-off title).
# Reachability treats him as located at offset 0.
NARRATOR = 'equiano'

HONORIFICS = {'mr', 'mrs', 'miss', 'ms', 'dr', 'doctor', 'rev', 'reverend', 'capt', 'captain',
              'hon', 'honourable', 'honorable', 'sir', 'lord', 'esq', 'admiral', 'general',
              'lieutenant', 'lieut', 'the'}
