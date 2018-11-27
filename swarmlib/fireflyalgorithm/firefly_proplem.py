# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

#pylint: disable=too-many-arguments
import logging

from swarmlib.fireflyalgorithm.firefly import Firefly

LOGGER = logging.getLogger(__name__)

class FireflyProblem():
    def __init__(self, firefly_number, function_dimension, upper_boundary, lower_boundary, alpha, beta, gamma, iteration_number):
        self.fireflies = []
        self.function_dimension = function_dimension
        self.upper_boundary = upper_boundary
        self.lower_boundary = lower_boundary
        self.iteration_number = iteration_number
        for _ in firefly_number:
            self.fireflies.append(Firefly(alpha, beta, gamma))

    def solve(self):
        for _ in self.iteration_number:
            pass
