# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import numpy as np
from ..util.coordinate import Coordinate


class Whale(Coordinate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__a = kwargs.get('a', 1.)
        self.__a_step_size = self.__a / kwargs['iteration_number']
        self.__b = kwargs.get('b', .5)

    def step(self, prey: Coordinate, rand_whale: Coordinate) -> None:
        """
        Execute a whale optimization step.
        Update the whale's position and value.

        Arguments:
            prey {Coordinate} -- The prey (global best whale)
            rand_whale {Coordinate} -- Randomly selected whale
        """
        prob: float = self._random.uniform()
        r_vec = self._random.uniform(size=2)  # Here r is in [0, 1) although the paper suggests [0, 1]
        a_vec = 2 * self.__a * r_vec - self.__a  # Equation 2.3
        c_vec = 2 * r_vec  # Equation 2.4

        if prob < 0.5:  # Equation 2.6
            if np.linalg.norm(a_vec) < 1:
                self.__encircle_prey(prey, a_vec, c_vec)
            else:
                self.__search_prey(rand_whale, a_vec, c_vec)
        else:
            self.__attack_prey(prey)

        self.__a -= self.__a_step_size

    def __search_prey(self, rand_whale: Coordinate, a_vec: np.ndarray, c_vec: np.ndarray) -> None:
        d_vec = np.linalg.norm(c_vec * rand_whale.position - self._position)  # Equation 2.7
        self._position = rand_whale.position - a_vec * d_vec  # Equation 2.8

    def __encircle_prey(self, prey: Coordinate, a_vec: np.ndarray, c_vec: np.ndarray):
        d_vec = np.linalg.norm(c_vec * prey.position - self._position)  # Equation 2.1
        self._position = prey.position - a_vec * d_vec  # Equation 2.2

    def __attack_prey(self, prey: Coordinate):
        d_vec = np.linalg.norm(prey.position - self._position)
        l_vec = self._random.uniform(size=2) # Here l is in [0, 1) although the paper suggests [0, 1]
        self._position = d_vec * np.exp(self.__b * l_vec) * np.cos(2 * np.pi * l_vec) + prey.position  # Equation 2.5
