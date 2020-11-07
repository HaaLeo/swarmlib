# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import logging

from .abc_problem import ABCProblem
from ..util.functions import FUNCTIONS

LOGGER = logging.getLogger(__name__)


def _run_abc(args):
    LOGGER.info('Start artificial bee colony with parameters="%s"', args)
    args['function'] = FUNCTIONS[args['function']]

    problem = ABCProblem(**args)
    problem.solve()
    problem.replay()


def configure_parser(sub_parsers):
    """
    Get the argument parser for artificial bee colony
    """

    parser = sub_parsers.add_parser(
        'bees',
        description='Solving an minimization problem using the artificial bee colony algorithm',
        help='artificial bee colony algorithm for minimization problem')

    parser.add_argument(
        '-f',
        '--function',
        type=str,
        default='michalewicz',
        help='''Choose the function that is used for searching the minimum.
        Choices are any of the 2D or nD single objective functions available
        in the 'landscapes' package (https://git.io/JTSFv). Example arguments:
        'michalewicz', 'ackley', 'rastrigin'.''',
        choices=[*FUNCTIONS],
        metavar='')
    parser.add_argument(
        '-u',
        '--upper-boundary',
        type=float,
        default=4.,
        help='Upper boundary of the function (default 4)')
    parser.add_argument(
        '-l',
        '--lower-boundary',
        type=float,
        default=0.,
        help='Lower boundary of the function (default 0)')

    parser.add_argument(
        '-n',
        '--iteration-number',
        type=int,
        default=30,
        help='Number of iterations to execute (default 30)')
    parser.add_argument(
        '-t',
        '--trials',
        type=int,
        default=3,
        help='Maximum number of trials a bee tries to find a new, better food source before it becomes exhausted.')
    parser.add_argument(
        '-a',
        '--alpha',
        type=float,
        default=1.,
        help='Scaling parameter used for levy flight step. (default 1)')
    parser.add_argument(
        '-la',
        '--lambda',
        type=float,
        default=1.5,
        help='Randomization parameter used for the levy flights distribution. (default 1.5)')

    parser.add_argument(
        'bees',
        type=int,
        help='Number of employed bees used for solving')

    parser.set_defaults(func=_run_abc)
