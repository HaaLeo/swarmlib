# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------


from .cuckoo_problem import CuckooProblem
from ..util.functions import FUNCTIONS

def _run_cuckoo_search(args):
    args['function'] = FUNCTIONS[args['function']]
    args['continuous'] = not bool(args['continuous'] == 'false' or args['continuous'] == 'f')
    problem = CuckooProblem(**args)
    problem.solve()

def configure_parser(sub_parsers):
    """
    Get the argument parser for the firefly algorithm
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
        help='Choose the function that is used for searching the minimum.',
        choices=['michalewicz', 'ackley'])
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
        type=int,
        default=1,
        help='Randomization parameter used for levy flights. (default 1)')
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
        '-i',
        '--interval',
        type=int,
        default=500,
        help='Interval between two animation frames in ms (default 500)')
    parser.add_argument(
        '-c',
        '--continuous',
        type=str,
        default='false',
        help='Indicates whether the algorithm should run continuously (default false)',
        choices=['false', 'f', 'true', 't'])

    parser.add_argument(
        'nests',
        type=int,
        help='Number of nests used for solving')

    parser.set_defaults(func=_run_cuckoo_search)
