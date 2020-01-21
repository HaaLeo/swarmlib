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
        self.__frame_interval = 50  # ms

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
        self.__positions.append([np.array(x_pos), np.array(y_pos)])

        vel_x, vel_y = zip(*particle_velocities)
        self.__velocities.append([np.array(vel_x), np.array(vel_y)])

    def replay(self):
        # Amount of frames to play considering the number of iterations to show and the __frame_interval update rate
        frames = int((self.__iteration_number+1)*self.__interval/self.__frame_interval)

        def __init():
            self.__particles.set_data([], [])

            self.__particle_vel.X = []
            self.__particle_vel.Y = []
            self.__particle_vel.XY = []
            self.__particle_vel.U = []
            self.__particle_vel.V = []

            self.__rectangle.set_edgecolor('none')

            return self.__particles, self.__rectangle, self.__particle_vel

        def __animate(i):
            marker_size = int(50 * self.__fig.get_figwidth()/self.__fig.dpi)
            self.__rectangle.set_edgecolor('k')
            ax = self.__fig.gca(label='myAxes')

            # Get the index of the current data to show
            index = int(np.floor(i / (frames/(self.__iteration_number+1))))
            self.__fig.canvas.set_window_title(f'Iteration {index}/{self.__iteration_number}')

            # Calculate the scale to apply to the data in order to generate a more dynamic visualization
            scale = (i-index*(frames/(self.__iteration_number+1))) / (frames/(self.__iteration_number+1))

            # Calculate scaled position and velocity
            x_data, y_data = self.__positions[index]
            vel_x, vel_y = self.__velocities[index+1]
            pos_x_scaled = np.clip(x_data + scale * vel_x, a_min=self.__lower_boundary, a_max=self.__upper_boundary)
            pos_y_scaled = np.clip(y_data + scale * vel_y, a_min=self.__lower_boundary, a_max=self.__upper_boundary)
            vel_x_scaled = (1-scale)*vel_x
            vel_y_scaled = (1-scale)*vel_y

            # Update the particle position
            self.__particles.set_data(pos_x_scaled, pos_y_scaled)
            self.__particles.set_markersize(marker_size)

            # Update the velocities
            self.__particle_vel = ax.quiver(pos_x_scaled, pos_y_scaled, vel_x_scaled, vel_y_scaled, angles='xy', scale_units='xy', scale=1, color='#CFCFCF', width=marker_size*0.001)

            return self.__particles, self.__rectangle, self.__particle_vel

        # iteration_number+1 for initialization frame
        _ = animation.FuncAnimation(self.__fig, __animate, frames=frames, interval=self.__frame_interval,
                                    blit=True, init_func=__init, repeat=self.__continuous)

        plt.show()
