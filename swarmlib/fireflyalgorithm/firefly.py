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
        self.__lower_boundary = lower_boundary
        self.__upper_boundary = upper_boundary

        self.__position = np.array([random.uniform(self.__lower_boundary, self.__upper_boundary)
                                    for _ in range(function_dimension)])

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def intensity(self):
        return self.__intensity

    def update_intensity(self, func):
        self.__intensity = -func(self.__position)

    def move_towards(self, better_position):
        # euclidean distance
        distance = np.linalg.norm(self.__position - better_position)

        # update position
        self.__position = self.__position + \
            self.__beta*np.exp(-self.__gamma*(distance**2)) * (better_position-self.__position) + \
            self.__alpha*(random.uniform(0, 1)-0.5)

        self.__check_boundaries()

    def random_walk(self, area):
        self.__position = np.array([random.uniform(cord-area, cord+area)
                                    for _, cord in np.ndenumerate(self.__position)])

    def __check_boundaries(self):
        for i, cord in np.ndenumerate(self.__position):
            if cord < self.__lower_boundary:
                self.__position[i] = self.__lower_boundary
            elif cord > self.__upper_boundary:
                self.__position[i] = self.__upper_boundary
            else:
                self.__position[i] = cord
