# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import logging

from .cuckoo_problem import CuckooProblem
from ..util.functions import FUNCTIONS

LOGGER = logging.getLogger(__name__)


def _run_cuckoo_search(args):
    LOGGER.info('Start cuckoo search with parameters="%s"', args)
    args['function'] = FUNCTIONS[args['function']]

    problem = CuckooProblem(**args)
    problem.solve()
    problem.replay()


def configure_parser(sub_parsers):
    """
    Get the argument parser for the cuckoo search algorithm
    """

    parser = sub_parsers.add_parser(
        'cuckoos',
        description='Solving an minimization problem using the cuckoo search algorithm',
        help='Cuckoo search algorithm for minimization problem')

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
        default=1.,
        help='Scaling parameter used for levy flight step. (default 1)')
    parser.add_argument(
        '-la',
        '--lambda',
        type=float,
        default=1.5,
        help='Randomization parameter used for the levy flights distribution. (default 1.5)')
    parser.add_argument(
        '-m',
        '--max-generations',
        type=int,
        default=10,
        help='Maximum number of generations. Number of iterations to execute (default 10)')
    parser.add_argument(
        '-p',
        '--p-a',
        type=float,
        default=.1,
        help='Fraction of nests that will be randomly abandoned after each iteration (default 0.1)')

    parser.add_argument(
        'nests',
        type=int,
        help='Number of nests used for solving')

    parser.set_defaults(func=_run_cuckoo_search)
