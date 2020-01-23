# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

# pylint: disable=too-many-instance-attributes

import logging

from .particle import Particle
from ..util.base_visualizer import BaseVisualizer
LOGGER = logging.getLogger(__name__)


class PSOProblem:
    def __init__(self, **kwargs):
        """
        Initialize a new particle swarm optimization problem.
        """

        self.__iteration_number = kwargs['iteration_number']
        self.__particles = [
            Particle(**kwargs)
            for _ in range(kwargs['particles'])
        ]

        # Initialize visualizer for plotting
        positions = [particle.position for particle in self.__particles]
        velocities = [particle.velocity for particle in self.__particles]
        self.__visualizer = BaseVisualizer(**kwargs)
        self.__visualizer.add_data(positions=positions, velocities=velocities)

    def solve(self):
        # Iterate to iteration_number+1 to generate iteration_number+1 velocities for visualization
        # And also update global_best_particle
        for _ in range(self.__iteration_number+1):

            # Update global best
            global_best_particle = min(self.__particles, key=lambda particle: particle.value)

            for particle in self.__particles:
                particle.step(global_best_particle.position)

            # Add data for plot
            positions = [particle.position for particle in self.__particles]
            velocities = [particle.velocity for particle in self.__particles]
            self.__visualizer.add_data(positions=positions, velocities=velocities)

        LOGGER.info('Last best solution="%s" at position="%s"', global_best_particle.value, global_best_particle.position)
        return global_best_particle

    def replay(self):
        """
        Start the problems visualization.
        """
        self.__visualizer.replay()
