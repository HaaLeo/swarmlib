# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

# pylint: disable=too-many-arguments,invalid-name,too-many-instance-attributes,too-many-locals

import logging
import operator
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import cm

from swarmlib.fireflyalgorithm.firefly import Firefly

LOGGER = logging.getLogger(__name__)


class FireflyProblem():
    def __init__(self, function, firefly_number, upper_boundary=4., lower_boundary=0., alpha=0.25, beta=1, gamma=0.97, iteration_number=10, interval=500, continuous=False):
        """Initializes a new instance of the `FireflyProblem` class.

        Arguments:  \r
        `firefly_number` -- Number of fireflies used for solving
        `function`       -- The 2D evaluation function. Its input is a 2D numpy.array  \r

        Keyword arguments:  \r
        `upper_boundary`   -- Upper boundary of the function (default 4)  \r
        `lower_boundary`   -- Lower boundary of the function (default 0)  \r
        `alpha`            -- Randomization parameter (default 0.25)  \r
        `beta`             -- Attractiveness at distance=0 (default 1)  \r
        `gamma`            -- Characterizes the variation of the attractiveness. (default 0.97) \r
        `iteration_number` -- Number of iterations to execute (default 100)  \r
        `interval`         -- Interval between two animation frames in ms (default 500)  \r
        `continuous`       -- Indicates whether the algorithm should run continuously (default False)
        """

        self.__alpha = alpha
        self.__beta = beta
        self.__gamma = gamma
        self.__function_dimension = 2
        self.__upper_boundary = upper_boundary
        self.__lower_boundary = lower_boundary
        self.__iteration_number = iteration_number
        self.__function = function
        self.__interval = interval
        self.__best = None
        self.__continuous = continuous
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

        if not self.__best or self.__fireflies[0].intensity > self.__best:
            self.__best = self.__fireflies[0].intensity

        LOGGER.info('Current best intensity: %s, Overall best intensity: %s',
                    self.__fireflies[0].intensity,
                    self.__best)

        # randomly walk the best firefly
        self.__fireflies[0].random_walk(0.1)
        self.__fireflies[0].update_intensity(self.__function)

    def solve(self):
        """Solve and visualize the problem."""
        x = np.linspace(self.__lower_boundary, self.__upper_boundary, 100)
        y = np.linspace(self.__lower_boundary, self.__upper_boundary, 100)
        X, Y = np.meshgrid(x, y)
        z = self.__function([X, Y])

        fig = plt.figure()

        ax = fig.add_subplot(1, 1, 1)
        cs = ax.contourf(X, Y, z, cmap=cm.PuBu_r)  # pylint: disable=no-member
        fig.colorbar(cs)

        x_init = []
        y_init = []
        for firefly in self.__fireflies:
            x_init.append(firefly.position[0])
            y_init.append(firefly.position[1])
        particles, = ax.plot(x_init, y_init, 'ro', ms=6)

        rectangle = plt.Rectangle([self.__lower_boundary, self.__lower_boundary],
                                  self.__upper_boundary-self.__lower_boundary,
                                  self.__upper_boundary-self.__lower_boundary,
                                  ec='none', lw=2, fc='none')
        ax.add_patch(rectangle)

        def __init():
            particles.set_data([], [])
            rectangle.set_edgecolor('none')
            return particles, rectangle

        def __animate(i):
            ms = int(50 * fig.get_figwidth()/fig.dpi)
            rectangle.set_edgecolor('k')
            x = []
            y = []
            fig.canvas.set_window_title(
                'Iteration %s/%s' % (i, self.__iteration_number))

            if i == 0:
                LOGGER.info('Reset fireflies')
                self.__best = None

            for idx, firefly in enumerate(self.__fireflies):
                # Reset fireflies after all iterations
                if i == 0:
                    firefly.position = np.array([x_init[idx], y_init[idx]])
                    firefly.update_intensity(self.__function)
                    fig.canvas.set_window_title('Initialization')
                x.append(firefly.position[0])
                y.append(firefly.position[1])
            self.__step()
            particles.set_data(x, y)
            particles.set_markersize(ms)

            return particles, rectangle

            # iteration_number+1 for initialization frame
        _ = animation.FuncAnimation(fig, __animate, frames=self.__iteration_number+1, interval=self.__interval,
                                    blit=True, init_func=__init, repeat=self.__continuous)

        plt.show()
