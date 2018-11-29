# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import logging
from matplotlib import pyplot as plt
import networkx as nx

LOGGER = logging.getLogger(__name__)


def draw_graph(graph, result):
    """Draw the given graph."""

    name = graph.name
    fig = plt.figure(name, clear=True)

    name += ' - Iteration (%s/%s) - ' % (
        result['current_iter'], result['total_iter'])

    if result['current_iter'] != result['total_iter']:
        name += 'processing...'
    else:
        name += 'done'

    fig.canvas.set_window_title(name)

    edge_widths = []
    edge_colors = []

    sorted_edges = [tuple(sorted((result['best_path'][idx], result['best_path'][idx+1])))
                    for idx in range(len(result['best_path'])-1)]

    for edge in graph.networkx_graph.edges():

        pheromone = graph.get_edge_pheromone(edge)

        edge_widths.append(pheromone)
        if edge in sorted_edges:
            edge_colors.append('b')
        else:
            edge_colors.append('black')

    nx.draw(
        graph.networkx_graph,
        pos=graph.node_coordinates,
        edge_color=edge_colors,
        width=__scale_range(edge_widths),
        with_labels=True)

    fig.canvas.flush_events()


def __scale_range(seq, new_max=5, new_min=0):
    old_max = max(seq)
    old_min = min(seq)
    return [(((old_value - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min for old_value in seq]
