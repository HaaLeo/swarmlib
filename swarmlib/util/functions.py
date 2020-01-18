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

    result = reduce(lambda acc, x: acc + func(x), x, 0.)
    return -result


def ackley(x, a=20, b=0.2, c=2*np.pi):

    x = np.asarray_chkfinite(x)  # ValueError if any NaN or Inf
    n = len(x)
    s1 = np.sum(x**2, axis=0)
    s2 = np.sum(np.cos(c * x), axis=0)
    return -a*np.exp(-b*np.sqrt(s1 / n)) - np.exp(s2 / n) + a + np.exp(1)


FUNCTIONS = {
    'michalewicz': michalewicz,
    'ackley': ackley
}
