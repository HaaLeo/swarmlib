# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch and contributors. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

# pylint: disable-msg=too-many-locals
from typing import Tuple

from ..util.coordinate import Coordinate


class Wolf(Coordinate):
    def step(self, a_parameter, alpha_pos: Tuple[float, float], beta_pos: Tuple[float, float],
             delta_pos: Tuple[float, float]) -> None:
        """
        Execute a wolf step.
        Update the wolf's position and value.

        Arguments:
            alpha_pos {Tuple[float, float]} -- The alpha position
            beta_pos {Tuple[float, float]} -- The beta position
            delta_pos {Tuple[float, float]} -- The delta position
        """


        r_1 = self._random.random()  # r_1 is a random number in [0,1]
        r_2 = self._random.random()  # r_2 is a random number in [0,1]

        a_1 = 2 * a_parameter * r_1 - a_parameter  # Equation (3.3)
        c_1 = 2 * r_2  # Equation (3.4)

        d_alpha = abs(c_1 * alpha_pos - self._position)  # Equation (3.5)-part 1
        x_1 = alpha_pos - a_1 * d_alpha  # Equation (3.6)-part 1

        r_1 = self._random.random()
        r_2 = self._random.random()

        a_2 = 2 * a_parameter * r_1 - a_parameter # Equation (3.3)
        c_2 = 2 * r_2  # Equation (3.4)

        d_beta = abs(c_2 * beta_pos - self._position)  # Equation (3.5)-part 2
        x_2 = beta_pos - a_2 * d_beta  # Equation (3.6)-part 2

        r_1 = self._random.random()
        r_2 = self._random.random()

        a_3 = 2 * a_parameter * r_1 - a_parameter  # Equation (3.3)
        c_3 = 2 * r_2  # Equation (3.4)

        d_delta = abs(c_3 * delta_pos - self._position)  # Equation (3.5)-part 3
        x_3 = delta_pos - a_3 * d_delta  # Equation (3.5)-part 3

        self._position = (x_1 + x_2 + x_3) / 3  # Equation (3.7)
