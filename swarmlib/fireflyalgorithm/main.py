# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from swarmlib.fireflyalgorithm.firefly_problem import FireflyProblem
from swarmlib.fireflyalgorithm.functions import michalewicz

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
        'firefly_number',
        type=int,
        help='Number of fireflies used for solving')

    parser.set_defaults(func=_run_firefly_algorithm)
