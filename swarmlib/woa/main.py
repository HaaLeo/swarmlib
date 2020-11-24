# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import logging

from .woa_problem import WOAProblem
from ..util.functions import FUNCTIONS

LOGGER = logging.getLogger(__name__)


def _run_woa(args):
    LOGGER.debug('Start the whale optimization algorithm with parameters="%s"', args)
    args['function'] = FUNCTIONS[args['function']]

    problem = WOAProblem(**args)
    problem.solve()
    problem.replay()


def configure_parser(sub_parsers):
    """
    Get the argument parser for the whale optimization algorithm.
    """

    parser = sub_parsers.add_parser(
        'whales',
        description='Solving an minimization problem using the whale optimization algorithm',
        help='Whale optimization algorithm for minimization problem')

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
        default=10,
        help='Number of iterations to execute (default 10)')
    parser.add_argument(
        '-a',
        '--a',
        type=float,
        default=1.,
        help='Controls the search\'s spread. (default 1)')
    parser.add_argument(
        '-b',
        '--b',
        type=float,
        default=.5,
        help='Controls the shape of the spiral which whale\'s follow. (default 0.5)')

    parser.add_argument(
        'whales',
        type=int,
        help='Number of whales used for solving')

    parser.set_defaults(func=_run_woa)
