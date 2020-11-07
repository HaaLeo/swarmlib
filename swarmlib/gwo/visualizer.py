# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch and contributors. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import numpy as np
from ..util.base_visualizer import BaseVisualizer


class Visualizer(BaseVisualizer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__best_wolf_indices = []

    def add_data(self, **kwargs) -> None:
        super().add_data(**kwargs)
        self.__best_wolf_indices.append(kwargs['best_wolf_indices'])

        # To show the static initial position first (without animation)
        if len(self.__best_wolf_indices) == 1:
            self.__best_wolf_indices.append(kwargs['best_wolf_indices'])

    def _animate(self, i: int, frames: int):
        self._marker_colors = np.full(len(self._positions[0][0]), self._marker_color)
        for index, color in zip(self.__best_wolf_indices[self._index], ['#39ff14', '#ffff33', '#654321']):
            self._marker_colors[index] = color

        return super()._animate(i, frames)
