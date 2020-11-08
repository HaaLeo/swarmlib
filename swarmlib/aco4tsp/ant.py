# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import logging
from threading import Thread
import numpy as np
from .local_2_opt import run_2opt
LOGGER = logging.getLogger(__name__)
# pylint: disable=attribute-defined-outside-init,too-many-instance-attributes,too-many-arguments,super-init-not-called,invalid-name


class Ant(Thread):
    def __init__(self, start_node, graph, alpha, beta, Q, use_2_opt, random):
        """Initializes a new instance of the Ant class."""
        self.initialize(start_node)
        self.graph = graph

        self.__alpha = alpha
        self.__beta = beta
        self.__Q = Q
        self.__use_2_opt = use_2_opt
        self._random = random

    def initialize(self, start_node):
        Thread.__init__(self)
        self.__current_node = start_node
        self.traveled_nodes = [self.__current_node]
        self.traveled_edges = []
        self.traveled_distance = 0
        self.selected_edge = None

    def run(self):
        """Run the ant."""
        # Possible locations where the ant can got to from the current node without the location it has already been.
        possible_locations = self.graph.get_connected_nodes(
            self.__current_node).difference(self.traveled_nodes)

        while possible_locations:
            self.__select_edge(possible_locations)
            self.__move_to_next_node(self.selected_edge)

            possible_locations = self.graph.get_connected_nodes(
                self.__current_node).difference(self.traveled_nodes)

        # Move back to origin
        self.__move_to_next_node((self.__current_node, self.traveled_nodes[0]))

        if self.__use_2_opt:
            self.traveled_nodes, self.traveled_distance = run_2opt(
                self.traveled_nodes,
                self.graph.get_edge_length)


    def __select_edge(self, possible_locations):
        """Select the edge where to go next."""
        LOGGER.debug('Possible locations="%s"', possible_locations)
        attractiveness = {}
        overall_attractiveness = .0
        for node in possible_locations:
            edge = (self.__current_node, node)

            edge_pheromone = self.graph.get_edge_pheromone(edge)
            # Gets the rounded distance.
            distance = self.graph.get_edge_length(edge)

            attractiveness[node] = pow(
                edge_pheromone, self.__alpha)*pow(1/distance, self.__beta)
            overall_attractiveness += attractiveness[node]

        if overall_attractiveness == 0:
            self.selected_edge = (self.__current_node,
                                  self._random.choice(list(attractiveness.keys())))
        else:
            choice = self._random.choice(list(attractiveness.keys()), p=list(attractiveness.values())/np.sum(list(attractiveness.values())))
            self.selected_edge = (self.__current_node, choice)

        LOGGER.debug('Selected edge: %s', (self.selected_edge,))

    def __move_to_next_node(self, edge_to_travel):
        """Move to the next node and update member."""
        self.traveled_distance += self.graph.get_edge_length(edge_to_travel)
        self.traveled_nodes.append(edge_to_travel[1])
        self.traveled_edges.append(edge_to_travel)
        LOGGER.debug('Traveled from node="%s" to node="%s". Overall traveled distance="%s"',
                     self.__current_node, edge_to_travel[1], self.traveled_distance)
        self.__current_node = edge_to_travel[1]

    def spawn_pheromone(self):
        # loop all except the last item
        for idx in range(len(self.traveled_nodes) - 1):
            traveled_edge = (
                self.traveled_nodes[idx], self.traveled_nodes[idx+1])
            pheromone = self.graph.get_edge_pheromone(traveled_edge)
            pheromone += self.__Q/self.graph.get_edge_length(traveled_edge)
            self.graph.set_pheromone(traveled_edge, pheromone)
