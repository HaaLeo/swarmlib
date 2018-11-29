# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import logging
import random
from threading import Thread, Event
from copy import deepcopy
from queue import Queue
import tsplib95
from matplotlib import pyplot as plt

from swarmlib.aco4tsp.ant import Ant
from swarmlib.aco4tsp.tsp_graph import Graph
from swarmlib.aco4tsp.sketcher import draw_graph

LOGGER = logging.getLogger(__name__)

# pylint: disable=too-many-instance-attributes,too-many-arguments,invalid-name,too-many-locals


class ACOProblem():
    def __init__(self, tsp_file, ant_number, rho=0.5, alpha=0.5, beta=0.5, q=1, iterations=100, plot_interval=10, two_opt=True):
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
        self.rho = rho  # evaporation rate
        self.alpha = alpha  # used for edge detection
        self.beta = beta  # used for edge detection
        self.Q = q  # Hyperparameter Q
        self.ant_number = ant_number  # Number of ants
        self.num_iterations = iterations  # Number of iterations
        self.plot_iter = plot_interval  # plot intervall
        self.__stop_event = Event()  # Event used to stop the plotting thread
        self.__result_queue = Queue()
        self.__last_result = None
        self.best_path = None
        self.shortest_distance = None
        self.__use_2_opt = two_opt

    def solve(self):
        """
        Solve the given problem.

        Returns `true` if problem was solved successfully otherwise `false`.
        """
        success = False
        args = deepcopy([self.ant_number, self.alpha, self.beta,
                         self.Q, self.rho, self.num_iterations, self.plot_iter, self.__use_2_opt])
        solving_thread = Thread(target=self.__solve, args=args)
        solving_thread.start()

        fig = plt.figure(self.__graph.name)

        try:
            while solving_thread.is_alive():
                self.__show_result()

                # Check whether plot was closed by user
                if not plt.fignum_exists(fig.number):
                    self.__stop_event.set()
                    break

            # Plot results that could be still queued
            while self.__result_queue.qsize() != 0:
                self.__show_result()

                # Check whether plot was closed by user
                if not plt.fignum_exists(fig.number):
                    self.__stop_event.set()
                    break

            if plt.fignum_exists(fig.number):
                success = True
        except KeyboardInterrupt:
            LOGGER.debug('The user closed the app. Stop calculation thread.')
            self.__stop_event.set()

        return success

    def __solve(self, ant_number, alpha, beta, Q, rho, num_iterations, plot_batch, use_2_opt):
        """Solve the problem."""
        ants = []
        shortest_distance = None
        best_path = None

        # Create ants
        for _ in range(ant_number):
            ant = Ant(random.choice(self.__graph.get_nodes()),
                      self.__graph, alpha, beta, Q, use_2_opt)
            ants.append(ant)

        for idx in range(num_iterations):
            # Start all multithreaded ants
            for ant in ants:
                ant.start()

            # Wait for all ants to finish
            for ant in ants:
                ant.join()

            # decay pheromone
            for edge in self.__graph.get_edges():
                pheromone = self.__graph.get_edge_pheromone(edge)
                pheromone *= 1-rho
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

            if self.__stop_event.is_set():
                LOGGER.debug('Stop event detected. Shut down thread.')
                break

            if (idx+1) % plot_batch == 0 or (idx+1) == num_iterations:
                self.__result_queue.put({
                    'best_path': best_path,
                    'current_iter': idx+1,
                    'total_iter': num_iterations
                })

        LOGGER.info('Finish! Shortest_distance="%s" and best_path="%s"',
                    shortest_distance, best_path)

    def show_result(self):
        """
        Plot the result using `matplotlib`.
        """

        self.__show_result(False)

    def __show_result(self, update=True):
        """Show the result. When update=True re-draw the figure if possible."""
        fig = plt.figure(self.__graph.name)

        if update:
            if self.__result_queue.qsize() != 0:
                self.__last_result = self.__result_queue.get()
                draw_graph(self.__graph, self.__last_result)
                self.__result_queue.task_done()

            plt.ion()
            fig.canvas.flush_events()
            plt.pause(0.01)

        else:
            plt.ioff()
            plt.show(block=True)
