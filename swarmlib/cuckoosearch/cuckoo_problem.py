# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------


class CuckooProblem:
    def __init__(self, **kwargs):
        self.__alpha = kwargs.get('alpha', 1)
        self.__continuous = kwargs.get('continuous', False)
        self.__interval = kwargs.get('interval', 1000)
        self.__upper_boundary = kwargs.get('upper_boundary', 4.)
        self.__lower_boundary = kwargs.get('lower_boundary', 0.)
        self.__max_generations = kwargs.get('max_generations', 10)
        self.__p_a = kwargs.get('p_a', .1)

        self.__function = kwargs['function']
        self.__nest_number = kwargs['nests']

    def solve(self):
        self.__function([1,1])
