# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import inspect
import logging
from os import path

import tsplib95

from .ant import Ant
from .tsp_graph import Graph
from .visualizer import Visualizer
from ..util.problem_base import ProblemBase

LOGGER = logging.getLogger(__name__)

# pylint: disable=too-many-instance-attributes,invalid-name,too-many-locals


class ACOProblem(ProblemBase):
    def __init__(self, **kwargs):
        """Initializes a new instance of the `ACOProblem` class.

        Arguments:  \r
        `ant_number` -- Number of ants used for solving

        Keyword arguments:  \r
        `tsp_file`   -- Path of the tsp file that shall be loaded  \r
        `rho`           -- Evaporation rate (default 0.5)  \r
        `alpha`         -- Relative importance of the pheromone (default 0.5)  \r
        `beta`          -- Relative importance of the heuristic information (default 0.5)  \r
        `q`             -- Constant Q. Used to calculate the pheromone, laid down on an edge (default 1)  \r
        `iterations`    -- Number of iterations to execute (default 10)  \r
        `plot_interval` -- Plot intermediate result after this amount of iterations (default 10) \r
        `two_opt`       -- Additionally use 2-opt local search after each iteration (default true)
        """
        super().__init__(**kwargs)
        self.__ant_number = kwargs['ant_number']  # Number of ants
        tsp_file = kwargs.get('tsp_file', path.join(path.abspath(path.dirname(inspect.getfile(inspect.currentframe()))), 'resources/burma14.tsp'))
        self.__graph = Graph(tsplib95.load_problem(tsp_file))
        LOGGER.info('Loaded tsp problem="%s"', tsp_file)

        self.__rho = kwargs.get('rho', 0.5)  # evaporation rate
        self.__alpha = kwargs.get('alpha', 0.5)  # used for edge detection
        self.__beta = kwargs.get('beta', 0.5)  # used for edge detection
        self.__Q = kwargs.get('q', 1)  # Hyperparameter Q
        self.__num_iterations = kwargs.get('iteration_number', 10)  # Number of iterations
        self.__use_2_opt = kwargs.get('two_opt', False)

        self._visualizer = Visualizer(**kwargs)

    def solve(self):
        """
        Solve the given problem.
        """

        ants = []
        shortest_distance = None
        best_path = None

        # Create ants
        ants = [
            Ant(self._random.choice(self.__graph.get_nodes()),
                self.__graph, self.__alpha, self.__beta, self.__Q, self.__use_2_opt, self._random)
            for _ in range(self.__ant_number)
        ]

        for _ in range(self.__num_iterations):
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
                ant.initialize(self._random.choice(self.__graph.get_nodes()))

            self._visualizer.add_data(
                best_path=best_path,
                pheromone_map={edge: self.__graph.get_edge_pheromone(edge) for edge in edges}
            )

        LOGGER.info('Finish! Shortest_distance="%s" and best_path="%s"',
                    shortest_distance, best_path)
        return best_path, shortest_distance

    def replay(self):
        """
        Play the visualization of the problem
        """
        self._visualizer.replay(graph=self.__graph)
