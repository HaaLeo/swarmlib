# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from copy import deepcopy
import logging

from .firefly import Firefly
from ..util.base_visualizer import BaseVisualizer
from ..util.problem_base import ProblemBase

LOGGER = logging.getLogger(__name__)


class FireflyProblem(ProblemBase):
    def __init__(self, **kwargs):
        """Initializes a new instance of the `FireflyProblem` class.

        Keyword arguments:  \r
        `firefly_number`   -- Number of fireflies used for solving
        `function`         -- The 2D evaluation function. Its input is a 2D numpy.array  \r
        `upper_boundary`   -- Upper boundary of the function (default 4)  \r
        `lower_boundary`   -- Lower boundary of the function (default 0)  \r
        `alpha`            -- Randomization parameter (default 0.25)  \r
        `beta`             -- Attractiveness at distance=0 (default 1)  \r
        `gamma`            -- Characterizes the variation of the attractiveness. (default 0.97) \r
        `iteration_number` -- Number of iterations to execute (default 100)  \r
        `interval`         -- Interval between two animation frames in ms (default 500)  \r
        `continuous`       -- Indicates whether the algorithm should run continuously (default False)
        """
        super().__init__(**kwargs)
        self.__iteration_number = kwargs.get('iteration_number', 10)
        # Create fireflies
        self.__fireflies = [
            Firefly(**kwargs, bit_generator=self._random)
            for _ in range(kwargs['firefly_number'])
        ]

        # Initialize visualizer for plotting
        self._visualizer = BaseVisualizer(**kwargs)
        self._visualizer.add_data(positions=[firefly.position for firefly in self.__fireflies])

    def solve(self) -> Firefly:
        """Solve the problem."""
        best = None
        for _ in range(self.__iteration_number):
            for i in self.__fireflies:
                for j in self.__fireflies:
                    if j < i:
                        i.move_towards(j.position)

            current_best = min(self.__fireflies)
            if not best or current_best < best:
                best = deepcopy(current_best)

            LOGGER.info('Current best value: %s, Overall best value: %s', current_best.value, best.value)

            # randomly walk the best firefly
            current_best.random_walk(0.1)

            # Add data for visualization
            self._visualizer.add_data(positions=[firefly.position for firefly in self.__fireflies])

        return best
