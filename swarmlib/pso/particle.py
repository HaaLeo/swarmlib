# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from typing import Tuple
import numpy as np

# pylint:disable=too-many-instance-attributes


class Particle:
    def __init__(self, **kwargs):
        self.__function = kwargs['function']
        self.__lower_boundary = kwargs['lower_boundary']
        self.__upper_boundary = kwargs['upper_boundary']
        self.__w = kwargs['weight']
        self.__c_1 = kwargs['c_1']
        self.__c_2 = kwargs['c_2']
        self.__max_velocity = kwargs['maximum_velocity']

        # Randomly create a new particle properties
        self.__position = np.random.uniform(self.__lower_boundary, self.__upper_boundary, 2)
        self.__value = self.__function(self.__position)
        self.__velocity = np.random.uniform(-1, 1, size=2)
        self.__clip_velocity()

        # Local best
        self.__best_position = self.__position
        self.__best_value = self.__value

    @property
    def position(self) -> Tuple[float, float]:
        return self.__position

    @property
    def value(self) -> float:
        return self.__value

    @property
    def velocity(self) -> float:
        return self.__velocity

    def step(self, global_best_pos: Tuple[float, float]) -> None:
        """
        Execute a particle step.
        Update the particle's velocity, position and value.

        Arguments:
            global_best_pos {Tuple[float, float]} -- The global best position
        """

        # Calculate velocity
        cognitive_velocity = self.__c_1 * np.random.random_sample(size=2) * (self.__best_position - self.__position)
        social_velocity = self.__c_2 * np.random.random_sample(size=2) * (global_best_pos - self.__position)
        self.__velocity = self.__w * self.__velocity + cognitive_velocity + social_velocity

        # Clip velocity to two
        self.__clip_velocity()

        # Update position and clip it to boundaries
        self.__position = np.clip(self.__position + self.__velocity, a_min=self.__lower_boundary, a_max=self.__upper_boundary)

        # Update value
        self.__value = self.__function(self.__position)

        # Update local best
        if self.__value < self.__best_value:
            self.__best_position = self.__position
            self.__best_value = self.__value

    def __clip_velocity(self):
        norm = np.linalg.norm(self.__velocity)
        if norm > self.__max_velocity:
            self.__velocity *= self.__max_velocity/norm
