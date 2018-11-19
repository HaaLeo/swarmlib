
import logging
import random
from threading import Thread, Event
from copy import deepcopy
from queue import Queue
import tsplib95
from matplotlib import pyplot as plt
import networkx as nx

from ant import Ant
from tsp_graph import Graph
LOGGER = logging.getLogger(__name__)


class ACOProblem(object):
    def __init__(self, tsp_file, ant_number, rho=0.5, alpha=0.5, beta=0.5, Q=0.01, num_iterations=1, plot_interval=1):
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
        self.plot_iter = plot_interval  # plot intervall
        self.stop_event = Event()  # Event used to stop the plotting thread
        self.solving_thread = None  # The thread used to solve the problem
        self.result_queue = Queue()

    def solve(self):
        args = deepcopy([self.ant_number, self.alpha, self.beta, self.Q, self.rho, self.num_iterations, self.plot_iter])
        self.solving_thread = Thread(target=self.__solve, args=args)
        self.solving_thread.start()

        try:
            while self.solving_thread.is_alive() and not self.stop_event.is_set():
                self.show_result()
        except:
            self.stop_event.set()

    def __solve(self, ant_number, alpha, beta, Q, rho, num_iterations, plot_batch):
        """Solve the problem."""
        ants = []
        shortest_distance = None
        best_path = None
        best_edge_seq = None

        # Create ants
        for _ in range(ant_number):
            ant = Ant(random.choice(self.graph.get_nodes()),
                      self.graph, alpha, beta, Q)
            ants.append(ant)

        for idx in range(num_iterations):
            # Start all multithreaded ants
            for ant in ants:
                ant.start()

            # Wait for all ants to finish
            for ant in ants:
                ant.join()

            # decay pheromone
            for edge in self.graph.get_edges():
                pheromone = self.graph.get_edge_pheromone(edge)
                pheromone *= 1-rho
                self.graph.set_pheromone(edge, pheromone)

            print(idx)
            # Add each ant's pheromone
            for ant in ants:
                ant.spawn_pheromone()

                # Check for best path
                if not shortest_distance or ant.traveled_distance < shortest_distance:
                    shortest_distance = ant.traveled_distance
                    best_path = ant.traveled_nodes
                    best_edge_seq = ant.traveled_edges
                    LOGGER.info('Updated shortest_distance="%s" and best_path="%s"',
                                shortest_distance, best_path)

                # Reset ants' thread
                ant.initialize(random.choice(self.graph.get_nodes()))


            if self.stop_event.is_set():
                break

            if (idx+1) % plot_batch == 0:
                self.result_queue.put({
                    'path_edges': best_edge_seq,
                    'best_path': best_path,
                    'wait': False,
                    'current_iter': idx+1,
                    'total_iter': num_iterations
                })
            elif idx == 0:
                self.result_queue.put({
                    'path_edges': best_edge_seq,
                    'best_path': best_path,
                    'current_iter': idx+1,
                    'total_iter': num_iterations
                })


        LOGGER.info('Finish! Shortest_distance="%s" and best_path="%s"',
                    shortest_distance, best_path)


    def show_result(self, block=False):
        """This plots the current state."""
        plt.ion()
        fig = plt.figure('dummy')

        if self.stop_event.is_set():
            return

        if not self.result_queue.empty():
            fig = plt.figure('dummy', clear=True)
            result = self.result_queue.get_nowait()

            name = self.graph.name
            if result['current_iter'] and result['total_iter']:
                name += ' - Iteration (%s/%s)' % (result['current_iter'], result['total_iter'])
            else:
                name+= ' - Final'

            G = self.graph.networkx_graph
            edge_widths = []
            edge_colors = []

            sorted_edges = [tuple(sorted(item)) for item in result['path_edges']]

            for edge in self.graph.networkx_graph.edges():

                pheromone = self.graph.get_edge_pheromone(edge)

                edge_widths.append(pheromone)
                if edge in sorted_edges:
                    edge_colors.append('b')
                else:
                    edge_colors.append('black')

            nx.draw(
                G,
                pos=self.graph.node_coordinates,
                edge_color=edge_colors,
                width=self.__scale_range(edge_widths),
                with_labels=True)

            fig.canvas.set_window_title(name)


        # throws an exception otherwise
        if not block:
            fig.canvas.flush_events()
            plt.pause(0.1)
        else:
            plt.ioff()
            plt.show(block)

    def __scale_range(self, seq, new_max=5, new_min=0):
        old_max = max(seq)
        old_min = min(seq)

        return [(((old_value - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min for old_value in seq]
