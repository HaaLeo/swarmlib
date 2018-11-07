import logging
from threading import Thread

LOGGER = logging.getLogger(__name__)


class Ant(Thread):
    def __init__(self, start_node, graph, alpha, beta):
        self.current_node = start_node
        self.graph = graph
        self.traveled_node = [start_node]
        self.alpha = alpha
        self.beta = beta
    def initialize_thread(self):
        Thread.__init__(self)

    def run(self):
        pass

    def _select_edge(self):
        # Possible locations where the ant can got to from the current node without the location it has already been.
        possible_locations = self.graph.get_connected_nodes(self.current_node).difference(self.traveled_node)
        LOGGER.debug('Possible locations="%s"', possible_locations)
        attractiveness = {}
        overall_attractiveness = .0
        for node in possible_locations:
            edge = (self.current_node, node)

            edge_pheromone = self.graph.get_edge_pheromone(edge)
            distance = self.graph.get_edge_length(edge) # Gets the rounded distance.

            attractiveness[node] = pow(edge_pheromone, self.alpha)*pow(1/distance, self.beta)
            overall_attractiveness += attractiveness
