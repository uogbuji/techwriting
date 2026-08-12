#!/usr/bin/env python
'''Project the extracted graph to networkx, run analytics, and write the results *back* as typed
Onya assertions — then query and render them.

Companion code for "Building and working knowledge graphs with Onya and LLMs" (the "The round trip:
analytics as first-class data" and "Seeing it" sections). Run `equiano_extract.py` first; this script
reads the graph it checkpointed to `equiano.db`.

The point of the round trip: centrality and community aren't left in an ephemeral figure — they land in
the graph as typed, merge-safe properties, queryable across sessions and re-extractions.

Prerequisites:
    pip install 'onya[nx]' matplotlib

Usage:
    python equiano_analyze.py
'''
import networkx
import matplotlib
matplotlib.use('Agg')   # headless-safe; drop this if you want an interactive window
import matplotlib.pyplot as plt

from onya.interp import value_of
from onya.serial import nx
from onya.store.sync import connect
from onya.terms import ONYA_INTERP

DOC_IRI = 'https://example.org/books/equiano-narrative'
NODEBASE = DOC_IRI + '/'
STORE_URL = 'sqlite:equiano.db'
ANALYTICS = 'https://example.org/analytics/'
IMAGE_OUT = 'equiano_kg.png'

# A small local model occasionally types a ship, a place, or a bare role as a Person (see the article's
# "'Fessing up" section). We drop that handful here so the social figure stays legible. Left in the
# graph, untouched — this filter is only for the analysis/figure.
NON_PERSON = {NODEBASE + n for n in (
    'CharmingSally', 'Andromache', 'Carcass', 'RaceHorse',      # ships
    'Jamaica', 'Delawar', 'WesterHall',                          # places
    'GrenadaPlanter', 'SlaveBelongingToMrRead', 'AfricanBrethren', 'Anglicania',  # roles / groups
)}


def main():
    with connect(STORE_URL) as store:
        g = store.get(DOC_IRI)
    g.merge()   # normalized view before projecting
    print(f'Loaded {len(g)} nodes from {STORE_URL}')

    # Project to networkx and keep the story's people (minus the handful of mis-typed non-persons).
    people = {str(n.id) for n in g.typematch('https://schema.org/Person')} - NON_PERSON
    mg = nx.to_networkx(g).subgraph(people).copy()

    # A memoir is an ego network: nearly everyone connects through the author, so the graph is one big
    # hub with a long tail of isolated mentions. Study the giant connected component — the actual web
    # of people who move through Equiano's life together.
    giant = mg.subgraph(max(networkx.connected_components(mg.to_undirected()), key=len)).copy()
    print(f'Giant component: {giant.number_of_nodes()} people, {giant.number_of_edges()} edges')

    betweenness = networkx.betweenness_centrality(giant)
    communities = networkx.community.louvain_communities(giant.to_undirected(), seed=42)
    community_of = {node: i for i, comm in enumerate(communities) for node in comm}
    print(f'{len(communities)} communities')

    # The trip home: results become typed, merge-safe Onya assertions. replace=True (the default) keeps
    # re-runs idempotent rather than accumulative.
    nx.write_back(g, ANALYTICS + 'betweenness', betweenness, interp=ONYA_INTERP('number'))
    nx.write_back(g, ANALYTICS + 'community', community_of, interp=ONYA_INTERP('number'))
    with connect(STORE_URL) as store:
        store.put(DOC_IRI, g, merge=True)

    # Queryable through the graph's own selector, with the number interpretation honored at the boundary.
    # The author's own node tops every centrality measure — definitional for a memoir, not an insight —
    # so the names just below it are the ones worth reading.
    print('\nTop betweenness:')
    top = sorted(g.select(label=ANALYTICS + 'betweenness'), key=value_of, reverse=True)[:8]
    for p in top:
        print(f'  {value_of(p):.4f}  {p.origin.id}')

    # The communities that actually cohere are the circles of a life.
    name = lambda nid: (giant.nodes[nid].get('https://schema.org/name') or [nid.rsplit('/', 1)[-1]])[0]
    print('\nCommunities:')
    for i, comm in enumerate(sorted(communities, key=len, reverse=True)):
        members = sorted(comm, key=lambda n: betweenness[n], reverse=True)
        print(f'  {i} ({len(comm)}): ' + ', '.join(name(m) for m in members[:8]))

    # Render — sized by centrality, colored by community, both read from the analysis we just did.
    sizes = [300 + 9_000 * betweenness[n] for n in giant.nodes]
    colors = [community_of[n] for n in giant.nodes]
    pos = networkx.spring_layout(giant, seed=42, k=0.7)
    labels = {n: name(n) for n in giant.nodes}

    plt.figure(figsize=(16, 9), dpi=150)
    networkx.draw_networkx_nodes(giant, pos, node_size=sizes, node_color=colors, cmap='tab10', alpha=0.9)
    networkx.draw_networkx_edges(giant, pos, alpha=0.2, arrows=False)
    networkx.draw_networkx_labels(giant, pos, labels=labels, font_size=7)
    plt.axis('off')
    plt.savefig(IMAGE_OUT, bbox_inches='tight')
    print(f'\nWrote {IMAGE_OUT}')
    # For a quick structural view without matplotlib: `onya convert equiano.onya.md > equiano.mmd`


if __name__ == '__main__':
    main()
