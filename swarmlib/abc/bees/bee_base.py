# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from typing import Tuple
from ...util.coordinate import Coordinate
from ...util.levy_flight import levy_flight


class BeeBase(Coordinate):

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new instance of the Bee class
        """
        super().__init__(**kwargs)
        self.__limit = kwargs.get('trials', 3)
        self.__lambda = kwargs.get('lambda', 1.5)
        self.__alpha = kwargs.get('alpha', 1.)
        self.__trials = 0
        self.__reset = True

    @property
    def is_reset(self) -> bool:
        """
        Indicates whether the bee is reset or not.

        Returns:
            bool: True if the bee was reset otherwise False
        """
        return self.__reset

    def reset(self) -> None:
        """
        Reset the bee if it exceeded the trial limit.
        """
        if self.__trials >= self.__limit:
            self._initialize()
            self.__trials = 0
            self.__reset = True

    def _explore(self, starting_position: Tuple[float, float], start_value: float) -> None:
        """
        Try to generate a new, position and save the better one

        Args:
            starting_position (Tuple[float, float]): The starting position
            start_value (float): The positions value
        """
        new_pos = levy_flight(starting_position, self.__alpha, self.__lambda)
        new_value = self._function(new_pos)

        if new_value < start_value:
            self._position = new_pos
            self.__trials = 0
            self.__reset = False
        else:
            self.__trials += 1
