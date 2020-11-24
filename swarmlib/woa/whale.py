# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import numpy as np
from ..util.coordinate import Coordinate


class Whale(Coordinate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__a = kwargs.get('a', 2.)
        self.__a_step_size = self.__a / kwargs['iteration_number']
        self.__b = kwargs.get('b', .5)

    def step(self, global_best_pos: np.ndarray) -> None:
        """
        Execute a whale optimization step.
        Update the whale's position and value.

        Arguments:
            global_best_pos {numpy.ndarray} -- The global best position
        """
        prob: float = self._random.uniform()
        r_vec = self._random.uniform(size=2)  # Here r is in [0, 1) although the paper suggests [0, 1]
        a_vec = 2 * self.__a * r_vec - self.__a  # Equation 2.3

        if prob > 0.5:  # Equation 2.6
            if np.linalg.norm(a_vec) < 1:
                self.__encircle_prey()
            else:
                self.__search_prey(global_best_pos, a_vec)
        else:
            self.__attack_prey()

    def __search_prey(self, global_best_pos: np.ndarray, a_vec: np.ndarray) -> None:
        c_vec = 2 * self._random.uniform(size=2)  # Equation 2.4
        d_vec = np.abs(c_vec * global_best_pos - self.__value)  # Equation 2.1
        self._position = global_best_pos - a_vec * d_vec  # Equation 2.2

    def __encircle_prey(self):
        pass

    def __attack_prey(self):
        pass
