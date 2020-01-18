# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from typing import Callable, Iterable, Tuple

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import cm
import numpy as np

# pylint:disable=too-many-locals,too-many-arguments


class Visualizer:
    def __init__(self, **kwargs):
        self.__lower_boundary = kwargs['lower_boundary']
        self.__upper_boundary = kwargs['upper_boundary']
        self.__function = kwargs['function']
        self.__iteration_number = kwargs['iteration_number']
        self.__interval = kwargs['interval']
        self.__continuous = kwargs['continuous']
        self.__nest_positions = []
        self.__iter_index = 1

        x = np.linspace(self.__lower_boundary, self.__upper_boundary, 100)
        y = np.linspace(self.__lower_boundary, self.__upper_boundary, 100)
        X, Y = np.meshgrid(x, y)
        z = self.__function([X, Y])

        self.__fig = plt.figure()

        ax = self.__fig.add_subplot(1, 1, 1)
        cs = ax.contourf(X, Y, z, cmap=cm.PuBu_r)  # pylint: disable=no-member
        self.__fig.colorbar(cs)
        self.__particles, = ax.plot([], [], 'ro', ms=6)

        self.__rectangle = plt.Rectangle([self.__lower_boundary, self.__lower_boundary],
                                         self.__upper_boundary-self.__lower_boundary,
                                         self.__upper_boundary-self.__lower_boundary,
                                         ec='none', lw=2, fc='none')
        ax.add_patch(self.__rectangle)

    def add_data(self, nest_positions: Iterable[Tuple[float, float]]) -> None:
        x_nest = [item[0] for item in nest_positions]
        y_nest = [item[1] for item in nest_positions]

        self.__nest_positions.append([x_nest, y_nest])

    def replay(self):
        def __init():
            self.__particles.set_data([], [])
            self.__rectangle.set_edgecolor('none')
            return self.__particles, self.__rectangle

        def __animate(i):
            ms = int(50 * self.__fig.get_figwidth()/self.__fig.dpi)
            self.__rectangle.set_edgecolor('k')
            self.__fig.canvas.set_window_title(
                'Generation %s/%s' % (i, self.__iteration_number))

            x_data, y_data = self.__nest_positions[i]
            self.__particles.set_data(x_data, y_data)
            self.__particles.set_markersize(ms)

            return self.__particles, self.__rectangle

            # iteration_number+1 for initialization frame
        _ = animation.FuncAnimation(self.__fig, __animate, frames=self.__iteration_number+1, interval=self.__interval,
                                    blit=True, init_func=__init, repeat=self.__continuous)

        plt.show()
