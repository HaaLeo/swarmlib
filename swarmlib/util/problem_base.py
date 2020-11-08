# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod
from numpy.random import default_rng
from ..util.coordinate import Coordinate
from ..util.visualizer_base import VisualizerBase

class ProblemBase(ABC):
    def __init__(self, **kwargs) -> None:
        self._random = default_rng(kwargs.get('seed', None))
        self._visualizer: VisualizerBase = None

    @abstractmethod
    def solve(self) -> Coordinate:
        pass

    def replay(self) -> None:
        """
        Start the problems visualization.
        """
        self._visualizer.replay()
