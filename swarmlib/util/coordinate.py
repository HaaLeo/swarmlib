# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from typing import Tuple

import numpy as np

class Coordinate:
    def __init__(self, **kwargs) -> None:
        """
        Initializes a new random coordinate.
        """
        self.__lower_boundary = kwargs.get('lower_boundary', 0.)
        self.__upper_boundary = kwargs.get('upper_boundary', 4.)
        self._random = kwargs['bit_generator']
        self._function = kwargs['function']

        self.__value = None
        self.__position = None
        self._initialize()

    def _initialize(self) -> None:
        """
        Initialize a new random position and its value
        """
        self._position = self._random.uniform(self.__lower_boundary, self.__upper_boundary, 2)

    @property
    def position(self) -> Tuple[float, float]:
        """
        Get the coordinate's position

        Returns:
            Tuple[float, float]: the Position
        """
        return self._position

    # Internal Getter
    @property
    def _position(self) -> Tuple[float, float]:
        return self.__position

    # Internal Setter for automatic position clipping and value update
    @_position.setter
    def _position(self, new_pos: Tuple[float, float]) -> None:
        """
        Set the coordinate's new position.
        Also updates checks whether the position is within the set boundaries
        and updates the coordinate's value.

        Args:
            value (Tuple[float, float]): The new coordinate position
        """
        self.__position = np.clip(new_pos, a_min=self.__lower_boundary, a_max=self.__upper_boundary)
        self.__value = self._function(self.__position)

    @property
    def value(self) -> float:
        return self.__value

    def __eq__(self, other):
        return self.__value == other.value
    def __ne__(self, other):
        return self.__value != other.value
    def __lt__(self, other):
        return self.__value < other.value
    def __le__(self, other):
        return self.__value <= other.value
    def __gt__(self, other):
        return self.__value > other.value
    def __ge__(self, other):
        return self.__value >= other.value
