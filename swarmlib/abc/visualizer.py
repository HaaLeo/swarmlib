# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import numpy as np

from ..util.base_visualizer import BaseVisualizer
# pylint:disable=too-many-locals,too-many-instance-attributes,invalid-name


class Visualizer(BaseVisualizer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        ax = self._fig.gca(label='BaseAxis')
        self.__best_bees_artist, = ax.plot([], [], 'o', color='#FFA500' if self._dark else '#ffff00', ms=6)
        self.__best_bees = [[], []]

        self.__onlooker_bee_positions = []
        self.__onlooker_bees_artist, = ax.plot([], [], 'o', color='darkblue' if self._dark else 'blue', ms=6)

        self._abandon_map = []

    def add_data(self, **kwargs) -> None:
        employee_positions, employee_reset = zip(*[(bee.position, bee.is_reset) for bee in kwargs['employee_bees']])
        kwargs['positions'] = employee_positions
        super().add_data(**kwargs)

        # Indicates whether the bee was generated this iteration or not
        self._abandon_map.append(np.array(employee_reset))

        # Handle onlooker_positions
        onlooker_positions = [bee.position for bee in kwargs['onlooker_bees']]

        self.__onlooker_bee_positions.append(np.transpose(onlooker_positions))

        # Handle best bee
        x_pos, y_pos = kwargs['best_position']
        self.__best_bees[0].append(x_pos)
        self.__best_bees[1].append(y_pos)

        # Initially add data twice
        if len(self.__onlooker_bee_positions) == 1:
            self._abandon_map.append(np.array(employee_reset))
            self.__onlooker_bee_positions.append(np.transpose(onlooker_positions))
            self.__best_bees[0].append(x_pos)
            self.__best_bees[1].append(y_pos)

    def _init(self):
        base_artists = super()._init()
        self.__best_bees_artist.set_data([], [])
        self.__onlooker_bees_artist.set_data([], [])

        return [*base_artists, self.__best_bees_artist, self.__onlooker_bees_artist]

    def _animate(self, i: int, frames: int):
        if self._index < len(self._abandon_map)-1:
            # Color the velocity different when the employee bee is abandoned
            self._vel_color = np.where(self._abandon_map[self._index+1], '#373737', '#CFCFCF')
        base_artists = super()._animate(i, frames)

        self.__best_bees_artist.set_data(self.__best_bees[0][:self._index], self.__best_bees[1][:self._index])
        self.__best_bees_artist.set_markersize(self._marker_size)

        x_pos, y_pos = self.__onlooker_bee_positions[self._index]
        self.__onlooker_bees_artist.set_data(x_pos, y_pos)
        self.__onlooker_bees_artist.set_markersize(self._marker_size)

        return [*base_artists, self.__best_bees_artist, self.__onlooker_bees_artist]
