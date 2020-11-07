# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import logging

from .pso_problem import PSOProblem
from ..util.functions import FUNCTIONS

LOGGER = logging.getLogger(__name__)


def _run_pso(args):
    LOGGER.info('Start particle swarm optimization with parameters="%s"', args)
    args['function'] = FUNCTIONS[args['function']]

    problem = PSOProblem(**args)
    problem.solve()
    problem.replay()


def configure_parser(sub_parsers):
    """
    Get the argument parser for particle swarm optimization
    """

    parser = sub_parsers.add_parser(
        'particles',
        description='Solving an minimization problem using the particle swarm optimization algorithm',
        help='Particle swarm optimization algorithm for minimization problem')

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
        '-w',
        '--weight',
        type=float,
        default=.5,
        help='Inertia weight balances the global and local search (default 0.5)')
    parser.add_argument(
        '-c1',
        '--c_1',
        type=float,
        default=2.,
        help='Scaling the "cognition" part of the velocity calculation (default 2)')
    parser.add_argument(
        '-c2',
        '--c_2',
        type=float,
        default=2.,
        help='Scaling the "social" part of the velocity calculation (default 2)')
    parser.add_argument(
        '-n',
        '--iteration-number',
        type=int,
        default=30,
        help='Number of iterations to execute (default 30)')
    parser.add_argument(
        '-v',
        '--maximum-velocity',
        type=float,
        default=2.,
        help='Maximum absolute velocity that is allowed for a particle (default 2.0)')

    parser.add_argument(
        'particles',
        type=int,
        help='Number of particles used for solving')

    parser.set_defaults(func=_run_pso)
