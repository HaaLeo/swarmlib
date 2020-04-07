# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from copy import deepcopy
from functools import reduce
import logging

import numpy as np

from .bees.employee_bee import EmployeeBee
from .bees.onlooker_bee import OnlookerBee
from .visualizer import Visualizer

LOGGER = logging.getLogger(__name__)

class ABCProblem():
    """Artificial Bee Colony Problem"""

    def __init__(self, **kwargs):
        """
        Initializes a new instance of the ABCProblem class.
        """

        self.__iteration_number = kwargs['iteration_number']
        self.__employee_bees = [
            EmployeeBee(**kwargs)
            for _ in range(kwargs['bees'])
        ]

        self.__onlooker_bees = [
            OnlookerBee(**kwargs)
            for _ in range(kwargs['bees'])
        ]

        self.__visualizer = Visualizer(**kwargs)

    def solve(self):
        """
        Solve the ABC problem
        """
        best = min(self.__employee_bees + self.__onlooker_bees, key=lambda bee: bee.value)
        self.__visualizer.add_data(employee_bees=self.__employee_bees, onlooker_bees=self.__onlooker_bees, best_position=best.position)

        # Iterate to iteration_number+1 to generate iteration_number+1 velocities for visualization
        for iteration in range(self.__iteration_number+1):
            # Employee bee phase
            for bee in self.__employee_bees:
                bee.explore()

            # Calculate the employee bees fitness values and probabilities
            overall_fitness = reduce(lambda acc, curr: acc + curr.fitness, self.__employee_bees, 0)
            employee_bees_fitness_probs = [bee.fitness/overall_fitness for bee in self.__employee_bees]

            # Choose the employee bees positions proportional to their fitness
            choices = np.random.choice(self.__employee_bees, size=len(self.__employee_bees), p=employee_bees_fitness_probs)

            # Onlooker phase
            # Explore new food sources based on the chosen employees' food sources
            for bee, choice in zip(self.__onlooker_bees, choices):
                bee.explore(choice.position, choice.value)

            # Scout phase
            for bee in self.__employee_bees + self.__onlooker_bees:
                bee.reset()

             # Update best food source
            current_best = min(self.__employee_bees + self.__onlooker_bees, key=lambda bee: bee.value)
            if current_best.value < best.value:
                best = deepcopy(current_best)
                LOGGER.info('Iteration %i Found new best solution="%s" at position="%s"', iteration+1, best.value, best.position)

            # Add data for plotting
            self.__visualizer.add_data(employee_bees=self.__employee_bees, onlooker_bees=self.__onlooker_bees, best_position=best.position)

        return best

    def replay(self):
        """
        Start the problems visualization.
        """
        self.__visualizer.replay()
