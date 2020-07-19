# Nimish Verma
from typing import Tuple
import numpy as np

from ..util.coordinate import Coordinate


class Wolf(Coordinate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def step(self, a, alpha_pos: Tuple[float, float], beta_pos: Tuple[float, float],
             delta_pos: Tuple[float, float]) -> None:
        """
        Execute a wolf step.
        Update the wolf's position and value.

        Arguments:
            alpha_pos {Tuple[float, float]} -- The alpha position
            beta_pos {Tuple[float, float]} -- The beta position
            delta_pos {Tuple[float, float]} -- The delta position
        """


        r_1 = np.random.random()  # r_1 is a random number in [0,1]
        r_2 = np.random.random()  # r_2 is a random number in [0,1]

        A_1 = 2 * a * r_1 - a  # Equation (3.3)
        C_1 = 2 * r_2  # Equation (3.4)

        D_alpha = abs(C_1 * alpha_pos - self._position);  # Equation (3.5)-part 1
        X1 = alpha_pos - A_1 * D_alpha;  # Equation (3.6)-part 1

        r_1 = np.random.random()
        r_2 = np.random.random()

        A_2 = 2 * a * r_1 - a;  # Equation (3.3)
        C_2 = 2 * r_2;  # Equation (3.4)

        D_beta = abs(C_2 * beta_pos - self._position);  # Equation (3.5)-part 2
        X2 = beta_pos - A_2 * D_beta;  # Equation (3.6)-part 2

        r_1 = np.random.random()
        r_2 = np.random.random()

        A_3 = 2 * a * r_1 - a;  # Equation (3.3)
        C_3 = 2 * r_2;  # Equation (3.4)

        D_delta = abs(C_3 * delta_pos - self._position);  # Equation (3.5)-part 3
        X3 = delta_pos - A_3 * D_delta;  # Equation (3.5)-part 3

        self._position = (X1 + X2 + X3) / 3  # Equation (3.7)
