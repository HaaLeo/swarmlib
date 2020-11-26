# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import numpy as np

from swarmlib.util.levy_flight import levy_flight

# pylint: disable=unused-variable


def describe_levy_flight():
    def is_calculated_correctly():
        result = levy_flight(np.array([1, 2]), 1, 1.5, np.random.default_rng(3))

        np.testing.assert_array_equal(result, [3.542576654276212, -0.5963111833259749])
