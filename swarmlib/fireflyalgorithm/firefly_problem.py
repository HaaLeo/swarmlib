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
    def __init__(self, function, firefly_number, function_dimension=1, upper_boundary=5, lower_boundary=-5, alpha=0.25, beta=1, gamma=0.97, iteration_number=10, plot_interval=10):
        self.__function_dimension = function_dimension
        self.__upper_boundary = upper_boundary
        self.__lower_boundary = lower_boundary
        self.__iteration_number = iteration_number
        self.__function = function
        self.__plot_interval = plot_interval

        # Create fireflies
        self.__fireflies = [Firefly(alpha, beta, gamma, self.__upper_boundary, self.__lower_boundary, self.__function_dimension)
                          for _ in range(firefly_number)]

        # Initialize intensity
        [firefly.update_intensity(self.__function) for firefly in self.__fireflies]

    def solve(self):
        self.__draw_function()
        for idx in range(self.__iteration_number):
            self.__step()

            if (idx+1) % self.__plot_interval == 0 or (idx+1) == self.__iteration_number:
                self.__update_positions()

        return True

    def __step(self):
        for i in self.__fireflies:
            for j in self.__fireflies:
                if j.intensity > i.intensity:
                    i.move_towards(j.position)
                    i.update_intensity(self.__function)

    @staticmethod
    def show_result():
        plt.show(block=True)

    def __update_positions(self):
        ax = plt.gca()
        positions = [firefly.position for firefly in self.__fireflies]
        intensities = [firefly.intensity for firefly in self.__fireflies]

        ax.scatter(*positions, intensities, color='green')


    def __draw_function(self):
        phi_m = np.linspace(self.__lower_boundary, self.__upper_boundary)
        phi_p = np.linspace(self.__lower_boundary, self.__upper_boundary)
        X, Y = np.meshgrid(phi_p, phi_m)

        Z = self.__function([X, Y])

        fig = plt.figure('MyFigure')

        # surface_plot with color grading and color bar
        axis = fig.add_subplot(1, 1, 1, projection='3d')
        axis.contour(X, Y, Z, zdir='z', offset=-5,
                     cmap=plt.cm.coolwarm)  # pylint: disable=no-member
        axis.set_zlim3d(self.__lower_boundary, self.__upper_boundary)
        p = axis.plot_surface(X, Y, Z, rstride=1, cstride=1,
                              cmap=plt.cm.coolwarm, linewidth=0, antialiased=False)  # pylint: disable=no-member
        fig.colorbar(p, shrink=0.5)


        positions = [firefly.position for firefly in self.__fireflies]
        intensities = [firefly.intensity for firefly in self.__fireflies]

        axis.scatter(*positions, intensities, color='green')
        plt.pause(0.5)
