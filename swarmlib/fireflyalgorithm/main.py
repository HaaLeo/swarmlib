# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------


from swarmlib.fireflyalgorithm.firefly_problem import FireflyProblem
from swarmlib.fireflyalgorithm.functions import FUNCTIONS

def _run_firefly_algorithm(args):
    args['function'] = FUNCTIONS[args['function']]
    args['continuous'] = False if args['continuous'] == 'false' or args['continuous'] == 'f' else True
    problem = FireflyProblem(**args)
    problem.solve()

def configure_parser(sub_parsers):
    """
    Get the argument parser for the firefly algorithm
    """

    parser = sub_parsers.add_parser(
        'fireflies',
        description='Solving an minimation problem using the firefly algorithm',
        help='Firefly algorithm for minimation problem')

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
        'firefly_number',
        type=int,
        help='Number of fireflies used for solving')

    parser.set_defaults(func=_run_firefly_algorithm)
