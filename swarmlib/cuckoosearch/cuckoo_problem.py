# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

# pylint: disable=too-many-instance-attributes

from copy import deepcopy
import logging

import numpy as np

from .nest import Nest
from ..util import levy_flight as cuckoo
from ..util.problem_base import ProblemBase
from .visualizer import Visualizer
LOGGER = logging.getLogger(__name__)


class CuckooProblem(ProblemBase):
    def __init__(self, **kwargs):
        """
        Initialize a new cuckoo search problem.
        """
        super().__init__(**kwargs)
        self.__upper_boundary = kwargs.get('upper_boundary', 4.)
        self.__lower_boundary = kwargs.get('lower_boundary', 0.)
        self.__alpha = kwargs.pop('alpha', 1)
        self.__max_generations = kwargs.pop('max_generations', 10)
        self.__lambda = kwargs.pop('lambda', 1.5)
        self.__p_a = kwargs.pop('p_a', .1)

        self.__function = kwargs['function']
        self.__nests = [
            Nest(lower_boundary=self.__lower_boundary, upper_boundary=self.__upper_boundary, function=self.__function, bit_generator=self._random)
            for _ in range(kwargs['nests'])
        ]

        # Initialize visualizer for plotting
        kwargs['iteration_number'] = self.__max_generations
        self._visualizer = Visualizer(**kwargs)

    def solve(self) -> Nest:
        nest_indices = np.array(range(len(self.__nests)))
        best_nest = deepcopy(min(self.__nests, key=lambda nest: nest.value))

        positions, abandoned = zip(*[(nest.position, nest.abandoned) for nest in self.__nests])
        self._visualizer.add_data(positions=positions, best_position=best_nest.position, abandoned=abandoned)

        LOGGER.info('Iteration 0 best solution="%s" at position="%s"', best_nest.value, best_nest.position)

        for iteration in range(self.__max_generations):

            # Perform levy flights to get cuckoo's new position
            new_cuckoo_pos = [
                np.clip(cuckoo.levy_flight(nest.position, self.__alpha, self.__lambda), a_min=self.__lower_boundary, a_max=self.__upper_boundary)
                for nest in self.__nests
            ]

            # Randomly select nests to be updated
            self._random.shuffle(nest_indices)

            # Update nests
            for index, pos in zip(nest_indices, new_cuckoo_pos):
                self.__nests[index].update_pos(pos)

            # Abandon nests randomly considering p_a
            for nest in self.__nests:
                if self._random.random() < self.__p_a:
                    nest.abandon()

            # Update best nest
            current_best = min(self.__nests)
            if current_best < best_nest:
                best_nest = deepcopy(current_best)
                LOGGER.info('Iteration %i Found new best solution="%s" at position="%s"', iteration+1, best_nest.value, best_nest.position)

            # Add data for plot
            positions, abandoned = zip(*[(nest.position, nest.abandoned) for nest in self.__nests])
            self._visualizer.add_data(positions=positions, best_position=current_best.position, abandoned=abandoned)

        LOGGER.info('Last best solution="%s" at position="%s"', best_nest.value, best_nest.position)
        return best_nest
