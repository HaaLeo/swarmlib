import logging
import sys
import argparse
import os

from aco4tsp.aco_problem import ACOProblem

logging.basicConfig(
    format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s',
    stream=sys.stdout,
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description='Solve a Traveling Salesman Problem using Ant Colony Optimization.')
    parser.add_argument(
        '-r',
        '--rho',
        type=float,
        default=.5,
        help='default=0.5')
    parser.add_argument(
        '-a',
        '--alpha',
        type=float,
        default=.5,
        help='default=0.5')
    parser.add_argument(
        '-b',
        '--beta',
        type=float,
        default=.5,
        help='default=0.5')
    parser.add_argument(
        '-q',
        '--q',
        type=float,
        default=1.,
        help='default=0.5')
    parser.add_argument(
        '-i',
        '--iterations',
        type=int,
        default=100,
        help='default=100')
    parser.add_argument(
        '-p',
        '--plot-interval',
        type=int,
        default=10,
        help='default=10')

    parser.add_argument(
        'tsp_file',
        type=str)
    parser.add_argument(
        'ant_number',
        type=int)
    args = parser.parse_args()

    if not os.path.isabs(args.tsp_file):
        args.tsp_file = os.path.join(os.getcwd(), args.tsp_file)

    problem = ACOProblem(**vars(args))
    if problem.solve():
        problem.show_result()


if __name__ == '__main__':
    main()
