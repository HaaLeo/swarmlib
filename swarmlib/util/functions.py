# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

#pylint: disable=invalid-name

import inspect
from functools import wraps

import landscapes.single_objective
import numpy as np


# Wrapper for landscapes.single_objective functions for inputs > 1d
def wrap_landscapes_func(landscapes_func):
    @wraps(landscapes_func)
    def wrapper(x):
        return np.apply_along_axis(func1d=landscapes_func, axis=0, arr=x)
    return wrapper


# Add all functions from landscapes.single_objective
FUNCTIONS = {
    name: wrap_landscapes_func(func)
    for (name, func) in inspect.getmembers(
        landscapes.single_objective, inspect.isfunction
    )
    if name not in ['colville', 'wolfe']  # Don't include 3D and 4D functions
}
