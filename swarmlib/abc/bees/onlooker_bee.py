# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from typing import Tuple
from .bee_base import BeeBase

class OnlookerBee(BeeBase):
    def explore(self, starting_position: Tuple[float, float], start_value: float) -> None:
        """
        Explore new food sources from the given one

        Args:
            starting_position ([type]): [description]
            start_value (float): [description]
        """
        self._explore(starting_position, start_value)
