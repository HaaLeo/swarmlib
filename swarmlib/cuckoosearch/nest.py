# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from typing import Tuple
import numpy as np


class Nest:
    def __init__(self, function, lower_boundary, upper_boundary):
        self.__function = function
        self.__lower_boundary = lower_boundary
        self.__upper_boundary = upper_boundary

        self.__position = np.random.uniform(self.__lower_boundary, self.__upper_boundary, 2)
        self.__value = self.__function(self.__position)

    @property
    def position(self) -> Tuple[float, float]:
        return self.__position

    @property
    def value(self) -> float:
        return self.__value

    def update_pos(self, new_position: Tuple[float, float]) -> None:
        """If the new position's value is better than the old one, update the nests position and value.

        Arguments:
            new_position {[type]} -- The new position
        """

        new_value = self.__function(new_position)
        if new_value < self.__value:
            self.__value = new_value
            self.__position = new_position
