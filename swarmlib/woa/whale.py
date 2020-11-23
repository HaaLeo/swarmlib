# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from typing import Tuple

from ..util.coordinate import Coordinate

class Whale(Coordinate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__a = kwargs.get('a', 2.)
        self.__a_step_size = self.__a / kwargs['iteration_number']
        self.__b = kwargs.get('b', .5)

    def step(self, global_best_pos: Tuple[float, float]) -> None:
        """
        Execute a whale optimization step.
        Update the whale's position and value.

        Arguments:
            global_best_pos {Tuple[float, float]} -- The global best position
        """
        probability: float = self._random.uniform()
        if probability > 0.5:

            if True: # Todo: |A| < 1
                self.__encircle_prey()
            else:
                self.__search_prey()
        else:
            self.__attack_prey()

    def __search_prey(self):
        pass

    def __encircle_prey(self):
        pass

    def __attack_prey(self):
        pass
