
import logging

import tsplib95
import matplotlib.pyplot as plt
import networkx as nx

from ant import Ant
from graph import Graph

LOGGER = logging.getLogger(__name__)

class ACOProblem(object):
    def __init__(self, tsp_file, ant_number, rho=0.1, alpha=0.5, beta=0.5, num_iterations=1000):
        """Initializes a new instance of the ACOProblem class."""
        self.graph = Graph(tsplib95.load_problem(tsp_file).get_graph())
        LOGGER.info('Loaded tsp problem="%s"', tsp_file)

        self.rho = rho # evaporation rate
        self.alpha = alpha # used for edge detection
        self.beta = beta # used for edge detection
        self.ant_number = ant_number # Number of ants
        self.num_iterations = num_iterations # Number of iterations

    def solve(self):
        """Solve the problem."""
        # Create ants
        self.ants = []
        for _ in range(self.ant_number):
            ant = Ant(1, self.graph)
            self.ants.append(ant)

        for _ in range(self.num_iterations):
            # Start all multithreaded ants
            for ant in self.ants:
                ant.start()

            # Wait for all ants to finish
            for ant in self.ants:
                ant.join()

            # TODO: Evaluate partial ant solutions

            # Reset ants
            for ant in self.ants:
                ant.__init__(ant.next_node, self.graph)

        nx.draw(self.graph.networkx_graph)
        plt.show()
