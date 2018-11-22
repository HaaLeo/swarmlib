import logging
import sys
import argparse
import os

from aco4tsp.aco_problem import ACOProblem
from aco4tsp._version import __version__

logging.basicConfig(
    format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s',
    stream=sys.stdout,
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)


def main():
    """
    usage: main.py [-h] [-r RHO] [-a ALPHA] [-b BETA] [-q Q] [-i ITERATIONS]
               [-p PLOT_INTERVAL]
               tsp_file ant_number

    Solve a Traveling Salesman Problem using Ant Colony Optimization.

    positional arguments:
    tsp_file              Path of the tsp file that shall be loaded
    ant_number            Number of ants used for solving

    optional arguments:
    -h, --help            show this help message and exit
    -r RHO, --rho RHO     Evaporation rate (default 0.5)
    -a ALPHA, --alpha ALPHA
                            Relative importance of the pheromone (default 0.5)
    -b BETA, --beta BETA  Relative importance of the heuristic information
                            (default 0.5)
    -q Q, --q Q           Constant Q. Used to calculate the pheromone, laid down
                            on an edge (default 1)
    -i ITERATIONS, --iterations ITERATIONS
                            Number of iterations to execute (default 100)
    -p PLOT_INTERVAL, --plot-interval PLOT_INTERVAL
                            Plot intermediate result after this amount of
                            iterations (default 10)
    """

    parser = argparse.ArgumentParser(
        description='Solve a Traveling Salesman Problem using Ant Colony Optimization.')
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
        '-v',
        '--version',
        action='version',
        version='%(prog)s v' + __version__,
        help='Show version and exit')

    parser.add_argument(
        'tsp_file',
        type=str,
        help='Path of the tsp file that shall be loaded')
    parser.add_argument(
        'ant_number',
        type=int,
        help='Number of ants used for solving')
    args = parser.parse_args()

    if not os.path.isabs(args.tsp_file):
        args.tsp_file = os.path.join(os.getcwd(), args.tsp_file)

    problem = ACOProblem(**vars(args))
    if problem.solve():
        problem.show_result()


if __name__ == '__main__':
    main()
