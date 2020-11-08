# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch and contributors. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import logging
from copy import deepcopy
import numpy as np
from .wolf import Wolf
from .visualizer import Visualizer
from ..util.problem_base import ProblemBase

# pylint: disable=too-many-instance-attributes

LOGGER = logging.getLogger(__name__)


class GWOProblem(ProblemBase):
    def __init__(self, **kwargs):
        """
        Initialize a new grey wolf optimization problem.
        """
        super().__init__(**kwargs)

        self.__iteration_number = kwargs.get('iteration_number', 30)
        self.__wolves = [
            Wolf(**kwargs, bit_generator=self._random)
            for _ in range(kwargs['wolves'])
        ]

        # Initialize visualizer for plotting
        best_indices = np.argsort(self.__wolves)[:3]
        positions = [wolf.position for wolf in self.__wolves]
        self._visualizer = Visualizer(**kwargs)
        self._visualizer.add_data(
            positions=positions,
            best_wolf_indices=best_indices)

    def solve(self) -> Wolf:

        # Initialization
        best = None
        best_indices = np.argsort(self.__wolves)[:3]
        alpha, beta, delta = [deepcopy(self.__wolves[index]) for index in best_indices]

        for iter_no in range(self.__iteration_number):
            a_parameter = 2 - iter_no * ((2) / self.__iteration_number)

            for wolf in self.__wolves:
                wolf.step(a_parameter, alpha.position, beta.position, delta.position)

            if not best or alpha < best:
                best = deepcopy(alpha)

            LOGGER.info('Current best value: %s, Overall best value: %s', alpha.value, best.value)

            # Add data for plot
            positions = [wolf.position for wolf in self.__wolves]
            self._visualizer.add_data(
                positions=positions,
                best_wolf_indices=best_indices)

            # Update alpha beta delta
            best_indices = np.argsort(self.__wolves)[:3]
            alpha, beta, delta = [deepcopy(self.__wolves[index]) for index in best_indices]

        return best
