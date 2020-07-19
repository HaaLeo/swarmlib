# Nimish Verma
import logging

from .wolf import Wolf
from ..util.base_visualizer import BaseVisualizer
from ..util.functions import FUNCTIONS
from .visualizer import Visualizer
from copy import deepcopy

LOGGER = logging.getLogger(__name__)


class GWOProblem:
    def __init__(self, **kwargs):
        """
        Initialize a new grey wolf optimization problem.
        """

        self.__iteration_number = kwargs.get('iteration_number', 20)
        self.__wolves = [
            Wolf(**kwargs)
            for _ in range(kwargs['wolves'])
        ]
        self.alpha, self.beta, self.delta = self.__wolves[:3]  # random alpha beta delta for initial coloring
        # Initialize visualizer for plotting
        positions = [wolf.position for wolf in self.__wolves]
        self.__visualizer = Visualizer(**kwargs)
        self.__visualizer.add_data(
            positions=positions)  # ,alpha_pos =self.alpha.position,beta_pos=self.beta.position,delta_pos=self.delta.position)

    def solve(self) -> Wolf:

        for iter_no in range(self.__iteration_number + 1):
            a = 2 - iter_no * ((2) / self.__iteration_number)
            # Update alpha beta delta
            self.__wolves.sort(key=lambda wolf: wolf.value)

            self.alpha, self.beta, self.delta = deepcopy(self.__wolves[:3])

            for particle in self.__wolves:
                particle.step(a, self.alpha.position, self.beta.position, self.delta.position)

            # Add data for plot
            positions = [particle.position for particle in self.__wolves]
            self.__visualizer.add_data(
                positions=positions)  # ,alpha_pos =self.alpha.position,beta_pos=self.beta.position,delta_pos=self.delta.position)

        LOGGER.info('Last best solution="%s" at position="%s"', self.alpha.value, self.alpha.position)
        return self.alpha

    def replay(self):
        """
        Start the problems visualization.
        """
        self.__visualizer.replay()

# print(GWOProblem(function=FUNCTIONS['michalewicz'], wolves=20, iteration_number=10))
