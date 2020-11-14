# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import numpy as np


import pytest

from swarmlib.util.coordinate import Coordinate

# pylint: disable=unused-variable


@pytest.fixture
def test_func():
    return lambda x: np.sum(x)  # pylint: disable=unnecessary-lambda


@pytest.fixture
def test_object(test_func):
    return Coordinate(
        function=test_func,
        bit_generator=np.random.default_rng(3),
        lower_boundary=0.1,
        upper_boundary=3.9)


def describe_coordinate():
    def describe_constructor():
        def describe_raise_error():
            def if_bit_generator_missing():
                with pytest.raises(KeyError):
                    Coordinate(function='foo')

            def if_function_is_missing():
                with pytest.raises(KeyError):
                    Coordinate(bit_generator='foo')

        def initializes_correctly(test_object):
            np.testing.assert_array_equal(test_object.position, [0.42546683514577255, 0.9998799250651788])
            np.testing.assert_equal(test_object.value, 1.4253467602109513)
            np.testing.assert_array_less(test_object.position, 3.9)
            np.testing.assert_array_less(0.1, test_object.position)

    def describe_comparison():
        @pytest.fixture
        def other(test_func):
            return Coordinate(
                function=test_func,
                bit_generator=np.random.default_rng(4),
                lower_boundary=0.1,
                upper_boundary=3.9)

        def equal(test_object):
            assert test_object == test_object  # pylint: disable=comparison-with-itself

        def not_equal(test_object, other):
            assert test_object != other

        def less(test_object, other):
            assert test_object < other

        def less_equal(test_object, other):
            assert test_object <= other
            assert test_object <= test_object  # pylint: disable=comparison-with-itself

        def greater(test_object, other):
            assert other > test_object

        def greater_equal(test_object, other):
            assert other >= test_object
            assert test_object >= test_object  # pylint: disable=comparison-with-itself

    def describe_position():
        def setter_clips_position_and_updates_value(test_object):
            test_object._position = [-5, 7]  # pylint: disable=protected-access

            np.testing.assert_array_equal(test_object.position, [0.1, 3.9])
            np.testing.assert_equal(test_object.value, 4)
