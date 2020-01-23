# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from typing import Tuple

from ..util.coordinate import Coordinate


class Nest(Coordinate):

    def update_pos(self, new_position: Tuple[float, float]) -> None:
        """
        If the new position's value is better than the old one, update the nests position and value.

        Arguments:
            new_position {Tuple[float, float]} -- The new position
        """

        new_value = self._function(new_position)
        if new_value < self._value:
            self._value = new_value
            self._position = new_position
