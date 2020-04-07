# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import numpy as np
from .bee_base import BeeBase


class EmployeeBee(BeeBase):
    def explore(self) -> None:
        """
        Explore new food sources from it's own position
        """
        self._explore(self._position, self.value)

    @property
    def fitness(self) -> float:
        """
        Get the fitness. Used for probability calculations

        Returns:
            float: the fitness
        """

        # Prefer negative values
        if self.value > 0:
            fitness = 1 / (self.value+1)  # shift the value by a constant
        else:
            fitness = np.abs(self.value) + 1

        return fitness
