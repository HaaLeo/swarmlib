# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

# pylint: disable=too-many-arguments

import numpy as np

from ..util.coordinate import Coordinate


class Firefly(Coordinate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__alpha = kwargs.get('alpha', 0.25)
        self.__beta = kwargs.get('beta', 1)
        self.__gamma = kwargs.get('gamma', 0.97)

    def move_towards(self, better_position):
        # euclidean distance
        distance = np.linalg.norm(self._position - better_position)

        # update position
        self._position = self._position + \
            self.__beta*np.exp(-self.__gamma*(distance**2)) * (better_position-self._position) + \
            self.__alpha*(self._random.uniform(0, 1)-0.5)

    def random_walk(self, area):
        self._position = np.array([self._random.uniform(cord-area, cord+area) for cord in self._position])
