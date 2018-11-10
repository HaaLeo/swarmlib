
import logging

import tsplib95

from ant import Ant
from tsp_graph import Graph

LOGGER = logging.getLogger(__name__)


class ACOProblem(object):
    def __init__(self, tsp_file, ant_number, rho=0.8, alpha=0.5, beta=0.5, Q=5, num_iterations=1):
        """Initializes a new instance of the ACOProblem class."""
        self.graph = Graph(tsplib95.load_problem(tsp_file))
        LOGGER.info('Loaded tsp problem="%s"', tsp_file)

        self.rho = rho  # evaporation rate
        self.alpha = alpha  # used for edge detection
        self.beta = beta  # used for edge detection
        self.ant_number = ant_number  # Number of ants
        self.num_iterations = num_iterations  # Number of iterations
        self.best_path = None
        self.shortest_distance = None
        self.Q = Q

    def solve(self):
        """Solve the problem."""
        # Create ants
        self.ants = []
        for _ in range(self.ant_number):
            ant = Ant(1, self.graph, self.alpha, self.beta, self.Q)
            self.ants.append(ant)

        for _ in range(self.num_iterations):
            # Start all multithreaded ants
            for ant in self.ants:
                ant.start()

            # Wait for all ants to finish
            for ant in self.ants:
                ant.join()

            # decay pheromone
            for edge in self.graph.get_edges():
                pheromone = self.graph.get_edge_pheromone(edge)
                pheromone *= 1-self.rho
                self.graph.set_pheromone(edge, pheromone)

            # Add each ant's pheromone
            for ant in self.ants:
                ant.spawn_pheromone()

                # Check for best path
                if not self.shortest_distance or ant.traveled_distance < self.shortest_distance:
                    self.shortest_distance = ant.traveled_distance
                    self.best_path = ant.traveled_nodes
                    self.best_edge_seq = ant.traveled_edges
                    LOGGER.info('Updated shortest_distance="%s" and best_path="%s"',
                                self.shortest_distance, self.best_path)

                # Reset ants' thread
                ant.initialize(1)

        LOGGER.info('Finish! Shortest_distance="%s" and best_path="%s"',
                    self.shortest_distance, self.best_path)

    def show_result(self):
        sorted_edges = [tuple(sorted(item)) for item in self.best_edge_seq]
        self.graph.show_result(sorted_edges, self.best_path)
