# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import logging
from copy import deepcopy
from threading import RLock
from tsplib95 import distances
import networkx as nx

LOGGER = logging.getLogger(__name__)


class Graph:
    def __init__(self, problem):
        self.__problem = problem
        self.__problem.wfunc = self.__distance  # do not round distances
        self.networkx_graph = self.__problem.get_graph()
        self.__lock = RLock()

    @property
    def node_coordinates(self):
        return self.__problem.node_coords

    @property
    def name(self):
        return deepcopy(self.__problem.comment)

    def get_nodes(self):
        """Get all nodes."""
        with self.__lock:
            return list(self.networkx_graph.nodes())

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
        sorted_edge = tuple(sorted(edge))
        return self.__get_edge_data(sorted_edge, 'pheromone')

    def get_edge_length(self, edge):
        """Get the `rounded` length of the given edge."""
        # tsplib95 stores the distance as "weight"
        return self.__get_edge_data(edge, 'weight')

    def __get_edge_data(self, edge, label):
        with self.__lock:
            data = self.networkx_graph.get_edge_data(*edge)
            result = deepcopy(data.get(label, 0))

        # LOGGER.debug('Get data="%s", value="%s" for edge="%s"',
        #              label, result, edge)
        return result

    def __distance(self, start, end):
        """
        This method is used to call the tsplib95's distance functions
        without rounding.
        """
        distance_function = distances.TYPES[self.__problem.edge_weight_type]
        return distance_function(start=self.__problem.node_coords[start], end=self.__problem.node_coords[end], round=lambda x: round(x, 2))
