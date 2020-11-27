# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from typing import Callable
import numpy as np
import pytest

from swarmlib.gwo.wolf import Wolf

# pylint: disable=unused-variable


@pytest.fixture
def test_func() -> Callable[[np.ndarray], float]:
    return lambda x: np.sum(x)  # pylint: disable=unnecessary-lambda


@pytest.fixture
def test_object(test_func) -> Wolf:
    return Wolf(
        function=test_func,
        bit_generator=np.random.default_rng(3))


def describe_wolf():
    def describe_step():
        def updates_position_correctly(test_object: Wolf):

            test_object.step(2.5, np.array([1, 1]), np.array([2, 2]), np.array([3, 3]))

            np.testing.assert_array_equal(test_object.position, [2.549101000158313, 2.42258339873344])
            np.testing.assert_equal(test_object.value, 4.971684398891753)
