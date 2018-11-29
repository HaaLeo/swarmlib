# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import logging
import os

from swarmlib.aco4tsp.aco_problem import ACOProblem

LOGGER = logging.getLogger(__name__)


def _run_aco4tsp(args):
    if not os.path.isabs(args['tsp_file']):
        args['tsp_file'] = os.path.join(os.getcwd(), args['tsp_file'])

    args['two_opt'] = False if args['two_opt'] == 'false' or args['two_opt'] == 'f' else True
    problem = ACOProblem(**args)
    if problem.solve():
        problem.show_result()


def configure_parser(sub_parsers):
    """
    Get the argument parser for the ant colony optimization algorithm
    """

    parser = sub_parsers.add_parser(
        'ants',
        description='Solve a traveling salesman problem using ant colony optimization',
        help='Ant colony optimization for the traveling salesman problem')

    parser.add_argument(
        '-r',
        '--rho',
        type=float,
        default=.5,
        help='Evaporation rate (default 0.5)')
    parser.add_argument(
        '-a',
        '--alpha',
        type=float,
        default=.5,
        help='Relative importance of the pheromone (default 0.5)')
    parser.add_argument(
        '-b',
        '--beta',
        type=float,
        default=.5,
        help='Relative importance of the heuristic information (default 0.5)')
    parser.add_argument(
        '-q',
        '--q',
        type=float,
        default=1.,
        help='Constant Q. Used to calculate the pheromone, laid down on an edge (default 1)')
    parser.add_argument(
        '-i',
        '--iterations',
        type=int,
        default=100,
        help='Number of iterations to execute (default 100)')
    parser.add_argument(
        '-p',
        '--plot-interval',
        type=int,
        default=10,
        help='Plot intermediate result after this amount of iterations (default 10)')
    parser.add_argument(
        '-o',
        '--two-opt',
        type=str,
        default='true',
        help='Additionally use 2-opt local search after each iteration (default true)',
        choices=['false', 'f', 'true', 't'])

    parser.add_argument(
        'tsp_file',
        type=str,
        help='Path of the tsp file that shall be loaded')
    parser.add_argument(
        'ant_number',
        type=int,
        help='Number of ants used for solving')

    parser.set_defaults(func=_run_aco4tsp)
