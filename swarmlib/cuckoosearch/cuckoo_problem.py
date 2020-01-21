# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

# pylint: disable=too-many-instance-attributes

import logging

import numpy as np

from .nest import Nest
from .cuckoo import Cuckoo
from .visualizer import Visualizer
LOGGER = logging.getLogger(__name__)


class CuckooProblem:
    def __init__(self, **kwargs):
        """
        Initialize a new cuckoo search problem.
        """

        self.__alpha = kwargs.get('alpha', 1)
        self.__continuous = kwargs.get('continuous', False)
        self.__interval = kwargs.get('interval', 1000)
        self.__upper_boundary = kwargs.get('upper_boundary', 4.)
        self.__lower_boundary = kwargs.get('lower_boundary', 0.)
        self.__max_generations = kwargs.get('max_generations', 10)
        self.__lambda = kwargs.get('lambda', 1.5)
        self.__p_a = kwargs.get('p_a', .1)

        self.__function = kwargs['function']
        self.__nests = [
            Nest(self.__function, self.__lower_boundary, self.__upper_boundary)
            for _ in range(kwargs['nests'])
        ]

        # Sort nests initally for best solution
        self.__nests.sort(key=lambda nest: nest.value)
        self.__best_nest = self.__nests[0]

        # Initialize visualizer for plotting
        kwargs['iteration_number'] = kwargs['max_generations']
        self.__visualizer = Visualizer(**kwargs)
        self.__visualizer.add_data([nest.position for nest in self.__nests], self.__nests[0].position)

    def solve(self):
        for _ in range(self.__max_generations):

            # Perform levy flights to get cuckoo's new position
            new_cuckoo_pos = [Cuckoo.levy_flight(nest.position, self.__alpha, self.__lambda) for nest in self.__nests]

            # Randomly select nests to be updated
            n_nests = len(self.__nests)
            nest_indices_to_update = np.random.randint(0, n_nests, n_nests)

            # Update nests
            for index in nest_indices_to_update:
                self.__nests[index].update_pos(new_cuckoo_pos[index])

            # Abandon nests randomly considering p_a
            self.__nests = [
                Nest(self.__function, self.__lower_boundary, self.__upper_boundary)
                if np.random.random_sample() < self.__p_a
                else nest
                for nest in self.__nests
            ]

            self.__nests.sort(key=lambda nest: nest.value)

            # Update best nest
            if self.__nests[0].value < self.__best_nest.value:
                self.__best_nest = self.__nests[0]
                LOGGER.info('Found new best solution="%s" at position="%s"', self.__best_nest.value, self.__best_nest.position)

            # Add data for plot
            data = [nest.position for nest in self.__nests]
            self.__visualizer.add_data(data, self.__nests[0].position)

        LOGGER.info('Last best solution="%s" at position="%s"', self.__best_nest.value, self.__best_nest.position)
        return self.__best_nest

    def replay(self):
        """
        Start the problems visualization.
        """
        self.__visualizer.replay()
