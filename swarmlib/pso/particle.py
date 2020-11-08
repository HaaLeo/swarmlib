# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from typing import Tuple
import numpy as np

from ..util.coordinate import Coordinate

# pylint: disable=too-many-instance-attributes


class Particle(Coordinate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__w = kwargs.get('weight', .5)
        self.__c_1 = kwargs.get('c_1', 2)
        self.__c_2 = kwargs.get('c_2', 2)
        self.__max_velocity = kwargs.get('maximum_velocity', 2)

        # Randomly create a new particle properties
        self.__velocity = self._random.uniform(-1, 1, size=2)
        self.__clip_velocity()

        # Local best
        self.__best_position = self._position
        self.__best_value = self.value

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
        cognitive_velocity = self.__c_1 * self._random.random(size=2) * (self.__best_position - self._position)
        social_velocity = self.__c_2 * self._random.random(size=2) * (global_best_pos - self._position)
        self.__velocity = self.__w * self.__velocity + cognitive_velocity + social_velocity

        # Clip velocity
        self.__clip_velocity()

        # Update position and clip it to boundaries
        self._position = self._position + self.__velocity

        # Update local best
        if self.value < self.__best_value:
            self.__best_position = self._position
            self.__best_value = self.value

    def __clip_velocity(self):
        norm = np.linalg.norm(self.__velocity)
        if norm > self.__max_velocity:
            self.__velocity *= self.__max_velocity/norm
