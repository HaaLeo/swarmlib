# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from matplotlib import animation
from matplotlib import pyplot as plt
import networkx as nx


def draw_graph(graph, results, dark, continuous, interval):
    """Draw the given graph."""

    if dark:
        plt.style.use('dark_background')
        node_color = '#0078D7'
        edge_color = 'white'
        best_edge_color = 'yellow'
    else:
        node_color = 'red'
        edge_color = 'black'
        best_edge_color = 'blue'

    fig, ax = plt.subplots(frameon=False)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    node_pos = graph.node_coordinates

    def update(num):
        ax.clear()

        fig.canvas.set_window_title(f'{graph.name} - Iteration ({num+1}/{len(results)})')

        edge_widths = []
        edge_colors = []

        sorted_edges = [
            tuple(sorted([
                results[num]['best_path'][idx],
                results[num]['best_path'][idx+1]
            ]))
            for idx in range(len(results[num]['best_path'])-1)
        ]

        for edge, pheromone in results[num]['edge_dict'].items():
            edge_widths.append(pheromone)
            if edge in sorted_edges:
                edge_colors.append(best_edge_color)
            else:
                edge_colors.append(edge_color)

        nx.draw_networkx_nodes(graph.networkx_graph, pos=node_pos, ax=ax, node_color=node_color)
        nx.draw_networkx_labels(graph.networkx_graph, pos=node_pos, ax=ax)
        nx.draw_networkx_edges(graph.networkx_graph, pos=node_pos, width=_scale_range(edge_widths), edge_color=edge_colors, ax=ax)

    _ = animation.FuncAnimation(fig, update, frames=len(results), interval=interval, repeat=continuous)
    plt.show()


def _scale_range(seq, new_max=5, new_min=0):
    old_max = max(seq)
    old_min = min(seq)
    return [(((old_value - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min for old_value in seq]
