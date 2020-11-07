# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import logging
from .firefly_problem import FireflyProblem
from ..util.functions import FUNCTIONS

LOGGER = logging.getLogger(__name__)


def _run_firefly_algorithm(args):
    LOGGER.info('Start firefly algorithm with parameters="%s"', args)
    args['function'] = FUNCTIONS[args['function']]

    problem = FireflyProblem(**args)
    problem.solve()
    problem.replay()


def configure_parser(sub_parsers):
    """
    Get the argument parser for the firefly algorithm
    """

    parser = sub_parsers.add_parser(
        'fireflies',
        description='Solving an minimization problem using the firefly algorithm',
        help='Firefly algorithm for minimization problem')

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
        '-a',
        '--alpha',
        type=float,
        default=0.25,
        help='Randomization parameter (default 0.25)')
    parser.add_argument(
        '-b',
        '--beta',
        type=float,
        default=1.,
        help='Attractiveness at distance=0 (default 1)')
    parser.add_argument(
        '-g',
        '--gamma',
        type=float,
        default=0.97,
        help='Characterizes the variation of the attractiveness. (default 0.97)')
    parser.add_argument(
        '-n',
        '--iteration-number',
        type=int,
        default=10,
        help='Number of iterations to execute (default 10)')

    parser.add_argument(
        'firefly_number',
        type=int,
        help='Number of fireflies used for solving')

    parser.set_defaults(func=_run_firefly_algorithm)
