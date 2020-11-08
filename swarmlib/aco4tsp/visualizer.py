# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from matplotlib import animation
from matplotlib import pyplot as plt
import networkx as nx

from ..util.visualizer_base import VisualizerBase

class Visualizer(VisualizerBase):  # pylint:disable=too-many-instance-attributes
    def __init__(self, **kwargs):
        self.__interval = kwargs.get('interval', 1000)
        self.__continuous = kwargs.get('continuous', False)
        dark = kwargs.get('dark', False)

        # The edge color and width per iteration
        self.__edge_widths = []
        self.__edge_colors = []

        if dark:
            plt.style.use('dark_background')
            self.__node_color = '#0078D7'
            self.__edge_color = 'white'
            self.__best_edge_color = 'yellow'
        else:
            self.__node_color = 'red'
            self.__edge_color = 'black'
            self.__best_edge_color = 'blue'

    def add_data(self, **kwargs):
        pheromone_map = kwargs['pheromone_map']
        best_path = kwargs['best_path']

        best_path_edges = [
            tuple(sorted([
                node,
                best_path[idx+1]
            ]))
            for idx, node in enumerate(best_path[:-1])
        ]

        self.__edge_widths.append(self.__scale_range(pheromone_map.values()))

        self.__edge_colors.append([
            self.__best_edge_color
            if edge in best_path_edges
            else self.__edge_color
            for edge in pheromone_map.keys()
        ])

    def replay(self, **kwargs):
        """Draw the given graph."""
        graph = kwargs['graph']
        fig, ax = plt.subplots(frameon=False)  # pylint:disable=invalid-name
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

        node_pos = graph.node_coordinates

        def _update(num):
            ax.clear()

            fig.canvas.set_window_title(f'{graph.name} - Iteration ({num+1}/{len(self.__edge_colors)})')

            nodes_artist = nx.draw_networkx_nodes(graph.networkx_graph, pos=node_pos, ax=ax, node_color=self.__node_color)
            labels_artist = nx.draw_networkx_labels(graph.networkx_graph, pos=node_pos, ax=ax)
            edges_artist = nx.draw_networkx_edges(graph.networkx_graph, pos=node_pos, width=self.__edge_widths[num], edge_color=self.__edge_colors[num], ax=ax)

            return nodes_artist, labels_artist, edges_artist

        _ = animation.FuncAnimation(fig, _update, frames=len(self.__edge_colors), interval=self.__interval, repeat=self.__continuous)
        plt.show()

    @staticmethod
    def __scale_range(seq, new_max=10, new_min=0.01):
        old_max = max(seq)
        old_min = min(seq)
        return [
            (((old_value - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min
            for old_value in iter(seq)
        ]
