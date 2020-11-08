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
        self.__best_nests_artist, = ax.plot([], [], 'o', color='#FFA500' if self._dark else '#ffff00', ms=6)
        self.__best_nests = [[], []]
        self._abandon_map = []

    def add_data(self, **kwargs) -> None:
        super().add_data(**kwargs)
        # Indicates whether the nest was generated this iteration or not
        abandoned = np.array(kwargs['abandoned'])
        self._abandon_map.append(abandoned)

        x_pos, y_pos = kwargs['best_position']
        self.__best_nests[0].append(x_pos)
        self.__best_nests[1].append(y_pos)

        # Initially add data twice
        if len(self.__best_nests) == 1:
            self._abandon_map.append(abandoned)
            self.__best_nests[0].append(x_pos)
            self.__best_nests[1].append(y_pos)

    def _init(self):
        base_artists = super()._init()
        self.__best_nests_artist.set_data([], [])

        return [*base_artists, self.__best_nests_artist]

    def _animate(self, i: int, frames: int):
        if self._index < len(self._abandon_map)-1:
            # Color the velocity different when the nest is abandoned
            self._vel_color = np.where(self._abandon_map[self._index+1], '#373737', '#CFCFCF')
        base_artists = super()._animate(i, frames)

        self.__best_nests_artist.set_data(self.__best_nests[0][:self._index], self.__best_nests[1][:self._index])
        self.__best_nests_artist.set_markersize(self._marker_size)

        return [*base_artists, self.__best_nests_artist]
