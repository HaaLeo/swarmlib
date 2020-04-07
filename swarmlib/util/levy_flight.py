# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from math import gamma
from typing import Tuple

import numpy as np


def levy_flight(start: Tuple[float, float], alpha: float, param_lambda: float) -> Tuple[float, float]:
    """
    Perform a levy flight step.

    Arguments:
        start {Tuple[float, float]} -- The cuckoo's start position
        alpha {float} -- The step size
        param_lambda {float} -- lambda parameter of the levy distribution

    Returns:
        Tuple[float, float] -- The new position
    """

    def get_step_length():
        dividend = gamma(1 + param_lambda) * np.sin(np.pi * param_lambda / 2)
        divisor = gamma((1 + param_lambda) / 2) * param_lambda * np.power(2, (param_lambda - 1) / 2)
        sigma1 = np.power(dividend / divisor, 1 / param_lambda)

        sigma2 = 1

        u_vec = np.random.normal(0, sigma1, size=2)
        v_vec = np.random.normal(0, sigma2, size=2)

        step_length = u_vec / np.power(np.fabs(v_vec), 1 / param_lambda)

        return step_length

    return start + alpha * get_step_length()
