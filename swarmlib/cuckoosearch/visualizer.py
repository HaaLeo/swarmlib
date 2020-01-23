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
        self.__best_nests_artist, = ax.plot([], [], 'o', color='#ffff00', ms=6)
        self.__best_nests = [[], []]

    def add_data(self, **kwargs) -> None:
        super().add_data(**kwargs)

        x_pos, y_pos = kwargs['best_position']
        self.__best_nests[0].append(x_pos)
        self.__best_nests[1].append(y_pos)

    def replay(self):
        # Prepare velocities before starting replay
        self._velocities = [self._positions[index+1]-position for index, position in enumerate(self._positions[:-1])]
        self._velocities.insert(0, np.zeros(self._positions[0].shape))
        self._velocities.append(np.zeros(self._positions[0].shape))

        super().replay()

    def _init(self):
        base_artists = super()._init()
        self.__best_nests_artist.set_data([], [])

        return [*base_artists, self.__best_nests_artist]

    def _animate(self, i: int, frames: int):
        base_artists = super()._animate(i, frames)

        self.__best_nests_artist.set_data(self.__best_nests[0][:self._index], self.__best_nests[1][:self._index])
        self.__best_nests_artist.set_markersize(self._marker_size)

        return [*base_artists, self.__best_nests_artist]
