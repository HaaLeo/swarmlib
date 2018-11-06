import logging
from copy import deepcopy
from threading import RLock
import networkx as nx
LOGGER = logging.getLogger(__name__)

class Graph:
    def __init__(self, graph):
        self.networkx_graph = graph
        self.__lock = RLock()

    def get_edges(self, node):
        """Get all edges with data connected to the given node. (u,v)"""
        with self.__lock:
            return self.networkx_graph.edges(node)

    def get_edge_pheromone(self, edge):
        """Get the pheromone value for the given edge"""
        with self.__lock:
            data = self.networkx_graph.get_edge_data(*edge)
            return deepcopy(data['pheromone'])

    def set_pheromone(self, edge, value):
        """Set pheromone for the given edge.
        Edge is tuple (u,v)"""
        with self.__lock:
            self.networkx_graph.add_edge(*edge, pheromone=value)

    def get_connected_nodes(self, node):
        """Get the connected nodes of the given node"""
        with self.__lock:
            return nx.node_connected_component(self.networkx_graph, node)
