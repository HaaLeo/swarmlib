# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch and contributors. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import numpy as np
from ..util.base_visualizer import BaseVisualizer

class Visualizer(BaseVisualizer):
    def replay(self):
        self._velocities = [self._positions[index+1]-position for index, position in enumerate(self._positions[:-1])]
        self._velocities.insert(0, np.zeros(self._positions[0].shape))
        self._velocities.append(np.zeros(self._positions[0].shape))
        super().replay()
