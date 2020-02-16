# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import logging
import random

import tsplib95

from .ant import Ant
from .tsp_graph import Graph
from .sketcher import draw_graph

LOGGER = logging.getLogger(__name__)

# pylint: disable=too-many-instance-attributes,too-many-arguments,invalid-name,too-many-locals


class ACOProblem():
    def __init__(self, tsp_file, ant_number, rho=0.5, alpha=0.5, beta=0.5, q=1, iteration_number=100, interval=1000, two_opt=True, dark=False, continuous=False):
        """Initializes a new instance of the `ACOProblem` class.

        Arguments:  \r
        `tsp_file`   -- Path of the tsp file that shall be loaded  \r
        `ant_number` -- Number of ants used for solving

        Keyword arguments:  \r
        `rho`           -- Evaporation rate (default 0.5)  \r
        `alpha`         -- Relative importance of the pheromone (default 0.5)  \r
        `beta`          -- Relative importance of the heuristic information (default 0.5)  \r
        `q`             -- Constant Q. Used to calculate the pheromone, laid down on an edge (default 1)  \r
        `iterations`    -- Number of iterations to execute (default 100)  \r
        `plot_interval` -- Plot intermediate result after this amount of iterations (default 10) \r
        `two_opt`       -- Additionally use 2-opt local search after each iteration (default true)
        """

        self.__graph = Graph(tsplib95.load_problem(tsp_file))
        LOGGER.info('Loaded tsp problem="%s"', tsp_file)
        self.__rho = rho  # evaporation rate
        self.__alpha = alpha  # used for edge detection
        self.__beta = beta  # used for edge detection
        self.__Q = q  # Hyperparameter Q
        self.__ant_number = ant_number  # Number of ants
        self.__num_iterations = iteration_number  # Number of iterations
        self.__result_data = []
        self.__best_path = None
        self.__shortest_distance = None
        self.__use_2_opt = two_opt

        self.__dark = dark
        self.__interval = interval
        self.__continuous = continuous

    def solve(self):
        """
        Solve the given problem.
        """

        ants = []
        shortest_distance = None
        best_path = None

        # Create ants
        ants = [
            Ant(random.choice(self.__graph.get_nodes()),
                self.__graph, self.__alpha, self.__beta, self.__Q, self.__use_2_opt)
            for _ in range(self.__ant_number)
        ]

        for idx in range(self.__num_iterations):
            # Start all multithreaded ants
            for ant in ants:
                ant.start()

            # Wait for all ants to finish
            for ant in ants:
                ant.join()

            # decay pheromone
            edges = self.__graph.get_edges()
            for edge in edges:
                pheromone = self.__graph.get_edge_pheromone(edge)
                pheromone *= 1-self.__rho
                self.__graph.set_pheromone(edge, pheromone)

            # Add each ant's pheromone
            for ant in ants:

                ant.spawn_pheromone()

                # Check for best path
                if not shortest_distance or ant.traveled_distance < shortest_distance:
                    shortest_distance = ant.traveled_distance
                    best_path = ant.traveled_nodes
                    LOGGER.info('Updated shortest_distance="%s" and best_path="%s"',
                                shortest_distance, best_path)

                # Reset ants' thread
                ant.initialize(random.choice(self.__graph.get_nodes()))

            self.__result_data.append({
                'best_path': best_path,
                'edge_dict': {edge: self.__graph.get_edge_pheromone(edge) for edge in edges}
            })

        LOGGER.info('Finish! Shortest_distance="%s" and best_path="%s"',
                    shortest_distance, best_path)
        return best_path, shortest_distance

    def replay(self):
        """
        Play the visualization of the problem
        """
        draw_graph(self.__graph, self.__result_data, self.__dark, self.__continuous, self.__interval)
