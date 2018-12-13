# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

#pylint:disable=import-error
#to do remove import-error

from fireflyalgorithm.firefly_problem import FireflyProblem
from fireflyalgorithm.functions import michalewicz

def _run_firefly_algorithm(args):
    if args['function'] == 'Michalewicz':
        args['function'] = michalewicz

    problem = FireflyProblem(**args)
    if problem.solve():
        problem.show_result()

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
        default='Michalewicz',
        help='Choose the function that is used for searching the minimum.',
        choices=['Michalewicz'])
    parser.add_argument(
        '-u',
        '--upper-boundary',
        type=float,
        default=4.,
        help='The upper boundary of the chosen function.')
    parser.add_argument(
        '-l',
        '--lower-boundary',
        type=float,
        default=0.,
        help='The lower boundary of the chosen function.')
    parser.add_argument(
        '-a',
        '--alpha',
        type=float,
        default=0.25,
        help='Alpha')
    parser.add_argument(
        '-b',
        '--beta',
        type=float,
        default=1.,
        help='Beta')
    parser.add_argument(
        '-g',
        '--gamma',
        type=float,
        default=0.97,
        help='Gamma')
    parser.add_argument(
        '-n',
        '--iteration-number',
        type=int,
        default=100,
        help='Number of iterations that will be executed.')
    parser.add_argument(
        '-i',
        '--interval',
        type=int,
        default=500,
        help='Interval between two animation frames in ms (default 500).')

    parser.add_argument(
        'firefly_number',
        type=int,
        help='Number of fireflies used for solving')

    parser.set_defaults(func=_run_firefly_algorithm)
