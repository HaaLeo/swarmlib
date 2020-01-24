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

        self.__upper_boundary = kwargs.get('upper_boundary', 4.)
        self.__lower_boundary = kwargs.get('lower_boundary', 0.)
        self.__alpha = kwargs.pop('alpha', 1)
        self.__max_generations = kwargs.pop('max_generations', 10)
        self.__lambda = kwargs.pop('lambda', 1.5)
        self.__p_a = kwargs.pop('p_a', .1)

        self.__function = kwargs['function']
        self.__nests = [
            Nest(lower_boundary=self.__lower_boundary, upper_boundary=self.__upper_boundary, function=self.__function)
            for _ in range(kwargs['nests'])
        ]

        # Sort nests initally for best solution
        self.__nests.sort(key=lambda nest: nest.value)
        self.__best_nest = self.__nests[0]

        # Initialize visualizer for plotting
        kwargs['iteration_number'] = self.__max_generations
        self.__visualizer = Visualizer(**kwargs)
        self.__visualizer.add_data(positions=[nest.position for nest in self.__nests], best_position=self.__nests[0].position)

    def solve(self):
        nest_indices = np.array(range(len(self.__nests)))
        for _ in range(self.__max_generations):

            # Perform levy flights to get cuckoo's new position
            new_cuckoo_pos = [
                np.clip(Cuckoo.levy_flight(nest.position, self.__alpha, self.__lambda), a_min=self.__lower_boundary, a_max=self.__upper_boundary)
                for nest in self.__nests
            ]

            # Randomly select nests to be updated
            np.random.shuffle(nest_indices)

            # Update nests
            for index in nest_indices:
                self.__nests[index].update_pos(new_cuckoo_pos[index])

            # Abandon nests randomly considering p_a
            self.__nests = [
                Nest(lower_boundary=self.__lower_boundary, upper_boundary=self.__upper_boundary, function=self.__function)
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
            self.__visualizer.add_data(positions=data, best_position=self.__nests[0].position)

        LOGGER.info('Last best solution="%s" at position="%s"', self.__best_nest.value, self.__best_nest.position)
        return self.__best_nest

    def replay(self):
        """
        Start the problems visualization.
        """
        self.__visualizer.replay()
