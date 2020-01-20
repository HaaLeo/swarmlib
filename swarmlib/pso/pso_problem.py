# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

# pylint: disable=too-many-instance-attributes

import logging

from .particle import Particle
from .visualizer import Visualizer
LOGGER = logging.getLogger(__name__)


class PSOProblem:
    def __init__(self, **kwargs):
        """
        Initialize a new cuckoo search problem.
        """

        # Args with defaults can be safely used afterwards
        args = {
            'iteration_number': kwargs.get('iteration_number', 30),
            'interval': kwargs.get('interval', 500),
            'continuous': kwargs.get('continuous', False),
            'lower_boundary': kwargs.get('lower_boundary', 0),
            'upper_boundary': kwargs.get('upper_boundary', 4),
            'weight': kwargs.get('weight', .5),
            'c_1': kwargs.get('c_1', 2),
            'c_2': kwargs.get('c_2', 2),
            'maximum_velocity': kwargs.get('maximum_velocity', 2),
            'function': kwargs['function'],
            'particles': kwargs['particles']
        }

        self.__iteration_number = args['iteration_number']
        self.__particles = [
            Particle(**args)
            for _ in range(args['particles'])
        ]

        # Initialize visualizer for plotting
        positions = [particle.position for particle in self.__particles]
        velocities = [particle.velocity for particle in self.__particles]
        self.__visualizer = Visualizer(**args)
        self.__visualizer.add_data(positions, velocities)

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
            self.__visualizer.add_data(positions, velocities)

        LOGGER.info('Last best solution="%s" at position="%s"', global_best_particle.value, global_best_particle.position)
        return global_best_particle

    def replay(self):
        """
        Start the problems visualization.
        """
        self.__visualizer.replay()
