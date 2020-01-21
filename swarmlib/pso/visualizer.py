# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from typing import Iterable, Tuple

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.cm import get_cmap
import numpy as np

# pylint:disable=too-many-locals,too-many-instance-attributes,invalid-name


class Visualizer:
    def __init__(self, **kwargs):
        self.__lower_boundary = kwargs['lower_boundary']
        self.__upper_boundary = kwargs['upper_boundary']
        self.__function = kwargs['function']
        self.__iteration_number = kwargs['iteration_number']
        self.__interval = kwargs['interval']
        self.__continuous = kwargs['continuous']
        self.__positions = []
        self.__velocities = []

        x = np.linspace(self.__lower_boundary, self.__upper_boundary, 100)
        y = np.linspace(self.__lower_boundary, self.__upper_boundary, 100)
        X, Y = np.meshgrid(x, y)
        z = self.__function([X, Y])

        self.__fig = plt.figure()

        ax = self.__fig.add_subplot(1, 1, 1, label='myAxes')
        cs = ax.contourf(X, Y, z, cmap=get_cmap('PuBu_r'))  # pylint: disable=no-member
        self.__fig.colorbar(cs)

        # Plot all particle pos
        self.__particles, = ax.plot([], [], 'ro', ms=6)

        # Plot all velocities
        self.__particle_vel = ax.quiver([], [], [], [], angles='xy', scale_units='xy', scale=1)

        self.__rectangle = plt.Rectangle([self.__lower_boundary, self.__lower_boundary],
                                         self.__upper_boundary-self.__lower_boundary,
                                         self.__upper_boundary-self.__lower_boundary,
                                         ec='none', lw=2, fc='none')
        ax.add_patch(self.__rectangle)

    def add_data(self, particle_positions: Iterable[Tuple[float, float]], particle_velocities: Iterable[Tuple[float, float]]) -> None:
        x_pos, y_pos = zip(*particle_positions)
        self.__positions.append([x_pos, y_pos])

        vel_x, vel_y = zip(*particle_velocities)
        self.__velocities.append([vel_x, vel_y])

    def replay(self):
        def __init():
            self.__particles.set_data([], [])
            ax = self.__fig.gca(label='myAxes')
            velocities = ax.quiver([], [], [], [], angles='xy', scale_units='xy', scale=1)
            self.__rectangle.set_edgecolor('none')
            return self.__particles, self.__rectangle, velocities

        def __animate(i):
            marker_size = int(50 * self.__fig.get_figwidth()/self.__fig.dpi)
            self.__rectangle.set_edgecolor('k')
            self.__fig.canvas.set_window_title(
                'Iteration %s/%s' % (i, self.__iteration_number))

            # Update the particle position
            x_data, y_data = self.__positions[i]
            self.__particles.set_data(x_data, y_data)
            self.__particles.set_markersize(marker_size)

            # Update the velocities
            ax = self.__fig.gca(label='myAxes')
            vel_x, vel_y = self.__velocities[i+1]
            velocities = ax.quiver(x_data, y_data, vel_x, vel_y, angles='xy', scale_units='xy', scale=1, color='#CFCFCF', width=marker_size*0.001)

            return self.__particles, self.__rectangle, velocities

            # iteration_number+1 for initialization frame
        _ = animation.FuncAnimation(self.__fig, __animate, frames=self.__iteration_number+1, interval=self.__interval,
                                    blit=True, init_func=__init, repeat=self.__continuous)

        plt.show()
