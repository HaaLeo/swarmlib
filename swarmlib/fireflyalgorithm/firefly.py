# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

# pylint: disable=too-many-arguments

import random
import numpy as np


class Firefly():
    def __init__(self, alpha, beta, gamma, upper_boundary, lower_boundary, function_dimension):
        self.__alpha = alpha
        self.__beta = beta
        self.__gamma = gamma
        self.__intensity = None

        self.__position = np.random.uniform(
            lower_boundary, upper_boundary, function_dimension)

    @property
    def position(self):
        return self.__position

    @property
    def intensity(self):
        return self.__intensity

    def update_intensity(self, func):
        self.__intensity = func(self.__position)

    def move_towards(self, better_position):
        # euclidean distance
        distance = np.linalg.norm(self.__position - better_position)

        # update position
        self.__position += self.__beta*np.exp(-self.__gamma*(distance**2)) * (better_position-self.__position) + \
            self.__alpha*(random.uniform(0, 1)-0.5)
