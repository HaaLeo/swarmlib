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


class BaseVisualizer:
    def __init__(self, **kwargs):
        self.__lower_boundary = kwargs.get('lower_boundary', 0.)
        self.__upper_boundary = kwargs.get('upper_boundary', 4.)
        self._iteration_number = kwargs.get('iteration_number', 10)
        self.__interval = kwargs.get('interval', 1000)
        self.__continuous = kwargs.get('continuous', False)

        self.__function = kwargs['function']

        self._marker_size = 0
        self._index = 0

        self._positions = []
        self._velocities = []
        self.__frame_interval = 50  # ms

        x = np.linspace(self.__lower_boundary, self.__upper_boundary, 100)
        y = np.linspace(self.__lower_boundary, self.__upper_boundary, 100)
        X, Y = np.meshgrid(x, y)
        z = self.__function([X, Y])

        self._fig = plt.figure()

        ax = self._fig.add_subplot(1, 1, 1, label='BaseAxis')
        cs = ax.contourf(X, Y, z, cmap=get_cmap('PuBu_r'))  # pylint: disable=no-member
        self._fig.colorbar(cs)

        # Plot all particle pos
        self.__particles, = ax.plot([], [], 'ro', ms=6)

        # Plot all velocities
        self.__particle_vel = ax.quiver([], [], [], [], angles='xy', scale_units='xy', scale=1)

        self.__rectangle = plt.Rectangle([self.__lower_boundary, self.__lower_boundary],
                                         self.__upper_boundary-self.__lower_boundary,
                                         self.__upper_boundary-self.__lower_boundary,
                                         ec='none', lw=2, fc='none')
        ax.add_patch(self.__rectangle)

    def add_data(self, **kwargs) -> None:
        positions: Iterable[Tuple[float, float]] = kwargs['positions']
        velocities: Iterable[Tuple[float, float]] = kwargs.get('velocities', np.zeros([len(kwargs['positions']), 2]))

        x_pos, y_pos = zip(*positions)
        self._positions.append(np.array([np.array(x_pos), np.array(y_pos)]))

        vel_x, vel_y = zip(*velocities)
        self._velocities.append([np.array(vel_x), np.array(vel_y)])

    def replay(self):
        # Amount of frames to play considering one interval should last __interval ms.
        frames = int((self._iteration_number+1)*self.__interval/self.__frame_interval)

        # iteration_number+1 for initialization frame
        animation.FuncAnimation(self._fig, self._animate, frames=frames, interval=self.__frame_interval,
                                blit=True, init_func=self._init, repeat=self.__continuous, fargs=[frames])

        plt.show()

    def _init(self):
        """
        Init function for animations. Only used for FuncAnimation
        """
        self.__particles.set_data([], [])

        self.__particle_vel.X = []
        self.__particle_vel.Y = []
        self.__particle_vel.XY = []
        self.__particle_vel.U = []
        self.__particle_vel.V = []

        self.__rectangle.set_edgecolor('none')

        return self.__particles, self.__rectangle, self.__particle_vel

    def _animate(self, i: int, frames: int):
        """
        Animation function for animations. Only used for FuncAnimation
        """

        self._marker_size = int(50 * self._fig.get_figwidth()/self._fig.dpi)
        self.__rectangle.set_edgecolor('k')
        ax = self._fig.gca(label='BaseAxis')

        # Get the index of the current data to show
        self._index = int(np.floor(i / (frames/(self._iteration_number+1))))
        self._fig.canvas.set_window_title(f'Iteration {self._index}/{self._iteration_number}')

        # Calculate the scale to apply to the data in order to generate a more dynamic visualization
        scale = (i-self._index*(frames/(self._iteration_number+1))) / (frames/(self._iteration_number+1))

        # Calculate scaled position and velocity
        x_data, y_data = self._positions[self._index]
        vel_x, vel_y = self._velocities[self._index+1]
        pos_x_scaled = np.clip(x_data + scale * vel_x, a_min=self.__lower_boundary, a_max=self.__upper_boundary)
        pos_y_scaled = np.clip(y_data + scale * vel_y, a_min=self.__lower_boundary, a_max=self.__upper_boundary)
        vel_x_scaled = (1-scale)*vel_x
        vel_y_scaled = (1-scale)*vel_y

        # Update the particle position
        self.__particles.set_data(pos_x_scaled, pos_y_scaled)
        self.__particles.set_markersize(self._marker_size)

        # Update the velocities
        self.__particle_vel = ax.quiver(pos_x_scaled, pos_y_scaled, vel_x_scaled, vel_y_scaled, angles='xy', scale_units='xy', scale=1, color='#CFCFCF', width=self._marker_size*0.001)

        return self.__particles, self.__rectangle, self.__particle_vel
