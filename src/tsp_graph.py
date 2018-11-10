import logging
from copy import deepcopy
from threading import RLock
from tsplib95 import distances
import matplotlib.pyplot as plt
import networkx as nx

LOGGER = logging.getLogger(__name__)

class Graph:
    def __init__(self, problem):
        self.__problem = problem
        self.__problem.wfunc = self.__distance # do not round distances
        self.networkx_graph = self.__problem.get_graph()
        self.__lock = RLock()

    def get_edges(self, node=None):
        """Get all edges connected to the given node. (u,v)"""
        with self.__lock:
            return self.networkx_graph.edges(node)

    def set_pheromone(self, edge, value):
        """Set pheromone for the given edge.
        Edge is tuple (u,v)"""
        with self.__lock:
            self.networkx_graph.add_edge(*edge, pheromone=value)

    def get_connected_nodes(self, node):
        """Get the connected nodes of the given node"""
        with self.__lock:
            return nx.node_connected_component(self.networkx_graph, node)

    def get_edge_pheromone(self, edge):
        """Get the pheromone value for the given edge"""
        return self.__get_edge_data(edge, 'pheromone')

    def get_edge_length(self, edge):
        """Get the `rounded` length of the given edge."""
        # tsplib95 stores the distance as "weight"
        return self.__get_edge_data(edge, 'weight')

    def show_result(self, path_edges, path_nodes):

        G = self.networkx_graph
        edge_widths = []
        edge_colors = []
        for edge in self.networkx_graph.edges():

            pheromone = self.get_edge_pheromone(edge)

            edge_widths.append(pheromone)
            if edge in path_edges:
                edge_colors.append('b')
            else:
                edge_colors.append('black')

        nx.draw(
            G,
            pos=self.__problem.node_coords,
            edge_color=edge_colors,
            width=self.__scale_range(edge_widths),
            with_labels=True,
            label=', '.join(str(path_nodes)))


        # labels = nx.get_edge_attributes(G, 'weight')
        # nx.draw_networkx_edge_labels(G, self.__problem.node_coords, edge_labels=labels)
        plt.show()

    def __get_edge_data(self, edge, label):
        with self.__lock:
            data = self.networkx_graph.get_edge_data(*edge)
            result=  deepcopy(data.get(label,0))

        LOGGER.debug('Get data="%s", value="%s" for edge="%s"', label, result, edge)
        return result

    def __distance(self, start, end):
        """
        This method is used to call the tsplib95's distance functions
        without rounding.
        """
        distance_function=distances.TYPES[self.__problem.edge_weight_type]
        return distance_function(start=self.__problem.node_coords[start], end=self.__problem.node_coords[end], round=lambda x: round(x,2))

    def __scale_range(self, seq, new_max=5, new_min=0):
        old_max = max(seq)
        old_min = min(seq)

        return [(((old_value - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min for old_value in seq]
