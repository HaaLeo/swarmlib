# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch and contributors. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import logging
from copy import deepcopy
from .wolf import Wolf
from .visualizer import Visualizer

# pylint: disable=too-many-instance-attributes

LOGGER = logging.getLogger(__name__)


class GWOProblem:
    def __init__(self, **kwargs):
        """
        Initialize a new grey wolf optimization problem.
        """

        self.__iteration_number = kwargs.get('iteration_number', 30)
        self.__wolves = [
            Wolf(**kwargs)
            for _ in range(kwargs['wolves'])
        ]
        self.__alpha, self.__beta, self.__delta = self.__wolves[:3]  # random alpha beta delta for initial coloring
        # Initialize visualizer for plotting
        positions = [wolf.position for wolf in self.__wolves]
        self.__visualizer = Visualizer(**kwargs)
        self.__visualizer.add_data(
            positions=positions)  # ,alpha_pos =self.alpha.position,beta_pos=self.beta.position,delta_pos=self.delta.position)

    def solve(self) -> Wolf:

        for iter_no in range(self.__iteration_number + 1):
            a_parameter = 2 - iter_no * ((2) / self.__iteration_number)
            # Update alpha beta delta
            self.__wolves.sort(key=lambda wolf: wolf.value)

            self.__alpha, self.__beta, self.__delta = deepcopy(self.__wolves[:3])

            for wolf in self.__wolves:
                wolf.step(a_parameter, self.__alpha.position, self.__beta.position, self.__delta.position)

            # Add data for plot
            positions = [particle.position for particle in self.__wolves]
            self.__visualizer.add_data(
                positions=positions)  # ,alpha_pos =self.alpha.position,beta_pos=self.beta.position,delta_pos=self.delta.position)

        LOGGER.info('Last best solution="%s" at position="%s"', self.__alpha.value, self.__alpha.position)
        return self.__alpha

    def replay(self):
        """
        Start the problems visualization.
        """
        self.__visualizer.replay()

# print(GWOProblem(function=FUNCTIONS['michalewicz'], wolves=20, iteration_number=10))
