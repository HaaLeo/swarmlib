# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod

class VisualizerBase(ABC):
    @abstractmethod
    def add_data(self) -> None:
        pass

    @abstractmethod
    def replay(self, **kwargs)-> None:
        pass
