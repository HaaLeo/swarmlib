# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

# pylint: disable=too-many-arguments,invalid-name,unused-import
import logging

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

from swarmlib.fireflyalgorithm.firefly import Firefly

LOGGER = logging.getLogger(__name__)


class FireflyProblem():
    def __init__(self, function, firefly_number, function_dimension=2, upper_boundary=5, lower_boundary=-5, alpha=0.25, beta=1, gamma=0.97, iteration_number=10):
        self.function_dimension = function_dimension
        self.upper_boundary = upper_boundary
        self.lower_boundary = lower_boundary
        self.iteration_number = iteration_number
        self. function = function
        # Create firefly_number random positions within the boundaries
        positions = np.random.uniform(
            lower_boundary, upper_boundary, (firefly_number, function_dimension))

        # Initialize fireflies
        self.fireflies = [Firefly(alpha, beta, gamma, position)
                          for position in positions]

    def solve(self):
        for _ in range(self.iteration_number):
            pass
        return True

    def show_result(self):
        phi_m = np.linspace(-5, 5)
        phi_p = np.linspace(-5, 5)
        X, Y = np.meshgrid(phi_p, phi_m)

        Z = self.function([X, Y])

        fig = plt.figure()

        # surface_plot with color grading and color bar
        axis = fig.add_subplot(1, 1, 1, projection='3d')
        axis.contour(X, Y, Z, zdir='z', offset=-5,
                     cmap=plt.cm.coolwarm)  # pylint: disable=no-member
        axis.set_zlim3d(-5, 5)
        p = axis.plot_surface(X, Y, Z, rstride=1, cstride=1,
                              cmap=plt.cm.coolwarm, linewidth=0, antialiased=False)  # pylint: disable=no-member
        fig.colorbar(p, shrink=0.5)
        plt.show(block=True)
