# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

# pylint: disable=too-many-instance-attributes

import logging

from .particle import Particle
from ..util.base_visualizer import BaseVisualizer
from ..util.problem_base import ProblemBase

LOGGER = logging.getLogger(__name__)


class PSOProblem(ProblemBase):
    def __init__(self, **kwargs):
        """
        Initialize a new particle swarm optimization problem.
        """
        super().__init__(**kwargs)
        self.__iteration_number = kwargs['iteration_number']
        self.__particles = [
            Particle(**kwargs, bit_generator=self._random)
            for _ in range(kwargs['particles'])
        ]

        # Initialize visualizer for plotting
        positions = [particle.position for particle in self.__particles]
        self._visualizer = BaseVisualizer(**kwargs)
        self._visualizer.add_data(positions=positions)

    def solve(self) -> Particle:
        # And also update global_best_particle
        for _ in range(self.__iteration_number):

            # Update global best
            global_best_particle = min(self.__particles)

            for particle in self.__particles:
                particle.step(global_best_particle.position)

            # Add data for plot
            positions = [particle.position for particle in self.__particles]
            self._visualizer.add_data(positions=positions)

        LOGGER.info('Last best solution="%s" at position="%s"', global_best_particle.value, global_best_particle.position)
        return global_best_particle
