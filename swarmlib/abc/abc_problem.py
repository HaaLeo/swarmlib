# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from copy import deepcopy
from functools import reduce
import logging

from .bees.employee_bee import EmployeeBee
from .bees.onlooker_bee import OnlookerBee
from .visualizer import Visualizer
from ..util.problem_base import ProblemBase

LOGGER = logging.getLogger(__name__)

class ABCProblem(ProblemBase):
    """Artificial Bee Colony Problem"""

    def __init__(self, **kwargs):
        """
        Initializes a new instance of the ABCProblem class.
        """
        super().__init__(**kwargs)
        self.__iteration_number = kwargs['iteration_number']
        self.__employee_bees = [
            EmployeeBee(**kwargs, bit_generator=self._random)
            for _ in range(kwargs['bees'])
        ]

        self.__onlooker_bees = [
            OnlookerBee(**kwargs, bit_generator=self._random)
            for _ in range(kwargs['bees'])
        ]

        self._visualizer = Visualizer(**kwargs)

    def solve(self):
        """
        Solve the ABC problem
        """
        best = min(self.__employee_bees + self.__onlooker_bees, key=lambda bee: bee.value)
        self._visualizer.add_data(employee_bees=self.__employee_bees, onlooker_bees=self.__onlooker_bees, best_position=best.position)

        for iteration in range(self.__iteration_number):
            # Employee bee phase
            for bee in self.__employee_bees:
                bee.explore()

            # Calculate the employee bees fitness values and probabilities
            overall_fitness = reduce(lambda acc, curr: acc + curr.fitness, self.__employee_bees, 0)
            employee_bees_fitness_probs = [bee.fitness/overall_fitness for bee in self.__employee_bees]

            # Choose the employee bees positions proportional to their fitness
            choices = self._random.choice(self.__employee_bees, size=len(self.__employee_bees), p=employee_bees_fitness_probs)

            # Onlooker phase
            # Explore new food sources based on the chosen employees' food sources
            for bee, choice in zip(self.__onlooker_bees, choices):
                bee.explore(choice.position, choice.value)

            # Scout phase
            for bee in self.__employee_bees + self.__onlooker_bees:
                bee.reset()

             # Update best food source
            current_best = min(self.__employee_bees + self.__onlooker_bees)
            if current_best < best:
                best = deepcopy(current_best)
                LOGGER.info('Iteration %i Found new best solution="%s" at position="%s"', iteration+1, best.value, best.position)

            # Add data for plotting
            self._visualizer.add_data(employee_bees=self.__employee_bees, onlooker_bees=self.__onlooker_bees, best_position=best.position)

        return best
