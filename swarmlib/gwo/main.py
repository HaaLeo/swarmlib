# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch and contributors. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------
import logging

from .gwo_problem import GWOProblem
from ..util.functions import FUNCTIONS

LOGGER = logging.getLogger(__name__)


def _run_gwo(args):
    LOGGER.info('Start grey wolf optimization with parameters="%s"', args)
    args['function'] = FUNCTIONS[args['function']]

    problem = GWOProblem(**args)
    problem.solve()
    problem.replay()


def configure_parser(sub_parsers):
    """
    Get the argument parser for grey wolf optimization
    """

    parser = sub_parsers.add_parser(
        'wolves',
        description='Solving an minimization problem using the grey wolf optimization algorithm',
        help='Grey Wolf optimization algorithm for minimization problem')

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
        help='Number of iterations to execute (default 30)')
    parser.add_argument(
        'wolves',
        type=int,
        help='Number of wolves used for solving')

    parser.set_defaults(func=_run_gwo)
