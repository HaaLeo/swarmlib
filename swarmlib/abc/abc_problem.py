# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from .bee import Bee
from ..util.base_visualizer import BaseVisualizer


class ABCProblem():
    """Artificial Bee Colony Problem"""

    def __init__(self, **kwargs):
        """
        Initializes a new instance of the ABCProblem class.
        """

        self.__iteration_number = kwargs['iteration_number']
        self.__bees = [
            Bee(**kwargs)
            for _ in range(kwargs['bees'])
        ]

        # Initialize visualizer for plotting
        positions = [bee.position for bee in self.__bees]
        velocities = [bee.velocity for bee in self.__bees]

        self.__visualizer = BaseVisualizer(**kwargs)
        self.__visualizer.add_data(positions=positions, velocities=velocities)

    def solve(self):
        """
        Solve the ABC problem
        """

    def replay(self):
        """
        Start the problems visualization.
        """
        self.__visualizer.replay()
