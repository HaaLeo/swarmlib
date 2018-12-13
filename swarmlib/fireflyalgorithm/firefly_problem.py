# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

# pylint: disable=too-many-arguments,invalid-name,too-many-instance-attributes,import-error,too-many-locals
#to do remove import-error
import logging
import operator
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import cm

from fireflyalgorithm.firefly import Firefly

LOGGER = logging.getLogger(__name__)


class FireflyProblem():
    def __init__(self, function, firefly_number, function_dimension=2, upper_boundary=4., lower_boundary=0., alpha=0.25, beta=1, gamma=0.97, iteration_number=100, interval=500):
        self.__alpha = alpha
        self.__beta = beta
        self.__gamma = gamma
        self.__function_dimension = function_dimension
        self.__upper_boundary = upper_boundary
        self.__lower_boundary = lower_boundary
        self.__iteration_number = iteration_number
        self.__function = function
        self.__interval = interval

        # Create fireflies
        self.__fireflies = [Firefly(self.__alpha,
                                    self.__beta,
                                    self.__gamma,
                                    self.__upper_boundary,
                                    self.__lower_boundary,
                                    self.__function_dimension)
                            for _ in range(firefly_number)]

        # Initialize intensity
        for firefly in self.__fireflies:
            firefly.update_intensity(self.__function)

    def __step(self):
        self.__fireflies.sort(
            key=operator.attrgetter('intensity'), reverse=True)
        for i in self.__fireflies:
            for j in self.__fireflies:
                if j.intensity > i.intensity:
                    i.move_towards(j.position)
                    i.update_intensity(self.__function)

        # randomly walk the best firefly
        self.__fireflies[0].random_walk(0.3)
        self.__fireflies[0].update_intensity(self.__function)

    def solve(self):
        x = np.linspace(self.__lower_boundary, self.__upper_boundary, 100)
        y = np.linspace(self.__lower_boundary, self.__upper_boundary, 100)
        X, Y = np.meshgrid(x, y)
        z = self.__function([X, Y])

        fig = plt.figure()

        ax = fig.add_subplot(1, 1, 1)
        cs = ax.contourf(X, Y, z, cmap=cm.PuBu_r)  # pylint: disable=no-member
        fig.colorbar(cs)

        x = []
        y = []
        for firefly in self.__fireflies:
            x.append(firefly.position[0])
            y.append(firefly.position[1])
        particles, = ax.plot(x, y, 'ro', ms=6)

        rectangle = plt.Rectangle([self.__lower_boundary, self.__lower_boundary],
                                  self.__upper_boundary-self.__lower_boundary,
                                  self.__upper_boundary-self.__lower_boundary,
                                  ec='none', lw=2, fc='none')
        ax.add_patch(rectangle)

        def __init():
            particles.set_data([], [])
            rectangle.set_edgecolor('none')
            return particles, rectangle

        def __animate(_):
            ms = int(fig.dpi * 2 * 0.02 * fig.get_figwidth()
                     / np.diff(ax.get_xbound())[0])
            rectangle.set_edgecolor('k')
            x = []
            y = []
            for firefly in self.__fireflies:
                x.append(firefly.position[0])
                y.append(firefly.position[1])
            self.__step()
            particles.set_data(x, y)
            particles.set_markersize(ms)

            return particles, rectangle

        _ = animation.FuncAnimation(fig, __animate, frames=self.__iteration_number, interval=self.__interval,
                                    blit=True, init_func=__init)
        # ani.save('videos/mich_firefly.mp4', fps=5,
        #          extra_args=['-vcodec', 'libx264'])

        plt.show()
