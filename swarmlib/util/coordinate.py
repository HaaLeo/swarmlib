# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from typing import Tuple

import numpy as np


class Coordinate:
    def __init__(self, **kwargs) -> None:
        self._lower_boundary = kwargs.get('lower_boundary', 0.)
        self._upper_boundary = kwargs.get('upper_boundary', 4.)
        self._function = kwargs['function']

        self._position = np.random.uniform(self._lower_boundary, self._upper_boundary, 2)
        self._value = self._function(self._position)

    @property
    def position(self) -> Tuple[float, float]:
        return self._position

    @property
    def value(self) -> float:
        return self._value
