# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from typing import Iterable, Tuple

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.cm import get_cmap
import numpy as np

from .visualizer_base import VisualizerBase
# pylint:disable=too-many-locals,too-many-instance-attributes,invalid-name


class BaseVisualizer(VisualizerBase):
    def __init__(self, **kwargs):
        self.__lower_boundary = kwargs.get('lower_boundary', 0.)
        self.__upper_boundary = kwargs.get('upper_boundary', 4.)
        self.__iteration_number = kwargs.get('iteration_number', 10)
        self.__intervals = self.__iteration_number + 2  # Two extra intervals for unanimated start and end pose
        self.__interval_ms = kwargs.get('interval', 1000)
        self.__continuous = kwargs.get('continuous', False)
        self._dark = kwargs.get('dark', False)

        self.__function = kwargs['function']

        self._marker_size = 0
        self._index = 0
        self._vel_color = '#CFCFCF'
        self._marker_color = '#0078D7' if self._dark else '#FF0000'
        self._marker_colors = np.empty(0)

        self._positions = []
        self._velocities = []
        self.__frame_interval = 50  # ms

        if self._dark:
            plt.style.use('dark_background')

        x = np.linspace(self.__lower_boundary, self.__upper_boundary, 400)
        y = np.linspace(self.__lower_boundary, self.__upper_boundary, 400)
        X, Y = np.meshgrid(x, y)
        z = self.__function([X, Y])

        self._fig = plt.figure()

        ax = self._fig.add_subplot(1, 1, 1, label='BaseAxis')
        cs = ax.contourf(X, Y, z, cmap=get_cmap('inferno' if self._dark else 'PuBu_r'))
        self._fig.colorbar(cs)

        # Plot all particle pos
        self.__particles = ax.scatter([], [], marker='o', zorder=2)

        # Plot all velocities
        self.__particle_vel = ax.quiver([], [], [], [], angles='xy', scale_units='xy', scale=1)

        self.__rectangle = plt.Rectangle([self.__lower_boundary, self.__lower_boundary],
                                         self.__upper_boundary-self.__lower_boundary,
                                         self.__upper_boundary-self.__lower_boundary,
                                         ec='none', lw=2, fc='none')
        ax.add_patch(self.__rectangle)

    def add_data(self, **kwargs) -> None:
        positions: Iterable[Tuple[float, float]] = kwargs['positions']

        self._positions.append(np.transpose(positions))

        if len(self._positions) == 1:
            # Insert the first position twice to show it "unanimated" first.
            self._positions.append(np.transpose(positions))

        # Calculate at time t the velocity for step t-1
        self._velocities.append(self._positions[-1] - self._positions[-2])

    def replay(self, **kwargs):
        # Overwrite last and first velocities with zeroes
        self._velocities.append(np.zeros(self._velocities[-1].shape))

        # Amount of frames to play considering one interval should last __interval ms.
        frames = int(self.__intervals*self.__interval_ms/self.__frame_interval)

        # iteration_number+1 for initialization frame
        _ = animation.FuncAnimation(self._fig, self._animate, frames=frames, interval=self.__frame_interval,
                                    blit=True, init_func=self._init, repeat=self.__continuous, fargs=[frames])

        plt.show()

    def _init(self):
        """
        Init function for animations. Only used for FuncAnimation
        """
        self.__particles.set_offsets([[]])
        self._marker_colors = np.full(len(self._positions[0][0]), self._marker_color)  # Create array of correct size
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
        self._index = int(np.floor(i / (frames/self.__intervals)))

        self._fig.canvas.set_window_title(f'Iteration {np.minimum(self._index, self.__iteration_number)}/{self.__iteration_number}')

        # Calculate the scale to apply to the data in order to generate a more dynamic visualization
        scale = i / (frames/self.__intervals) - self._index

        # Calculate scaled position and velocity
        pos = self._positions[self._index]
        vel = self._velocities[self._index]
        pos_scaled = np.clip(pos + scale * vel, a_min=self.__lower_boundary, a_max=self.__upper_boundary)
        vel_scaled = (1-scale)*vel

        # Update the particle position
        self.__particles.set_offsets(np.transpose(pos_scaled))
        self.__particles.set_sizes(np.full(len(pos_scaled[0]), self._marker_size**2))
        self.__particles.set_color(self._marker_colors)

        # Update the velocities
        self.__particle_vel = ax.quiver(pos_scaled[0], pos_scaled[1], vel_scaled[0], vel_scaled[1], angles='xy', scale_units='xy', scale=1, color=self._vel_color, width=self._marker_size*0.001)

        return self.__particles, self.__rectangle, self.__particle_vel
