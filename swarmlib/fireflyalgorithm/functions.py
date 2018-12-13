# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

#pylint: disable=invalid-name

from functools import reduce
import numpy as np


def michalewicz(x):
    m = 10
    def func(x):
        return np.sin(x) * np.power(np.sin((0 + 1) * np.power(x, 2) / np.pi), 2 * m)

    result = reduce((lambda acc, x: acc + func(x)), x, 0.)
    return -result
