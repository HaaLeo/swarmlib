# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from typing import Tuple

from ..util.coordinate import Coordinate


class Nest(Coordinate):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__abandoned = True

    @property
    def abandoned(self) -> bool:
        """
        Indicates whether a nest was abandoned or not

        Returns:
            bool: True the nest was abandoned otherwise False
        """
        return self.__abandoned

    def abandon(self) -> None:
        self.__abandoned = True
        self._initialize()

    def update_pos(self, new_position: Tuple[float, float]) -> None:
        """
        If the new position's value is better than the old one, update the nests position and value.

        Arguments:
            new_position {Tuple[float, float]} -- The new position
        """

        new_value = self._function(new_position)
        if new_value < self.value:
            if self.__abandoned:
                self.__abandoned = False
            # Value is updated automatically in base class
            self._position = new_position
