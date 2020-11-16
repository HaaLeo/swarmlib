# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

import logging
import sys
import argparse


from .aco4tsp.main import configure_parser as aco_parser
from .fireflyalgorithm.main import configure_parser as firefly_parser
from .cuckoosearch.main import configure_parser as cuckoo_parser
from .pso.main import configure_parser as pso_parser
from .abc.main import configure_parser as abc_parser
from .gwo.main import configure_parser as gwo_parser
from ._version import __version__


def run_swarm():
    parser = argparse.ArgumentParser(
        description='Solve an optimization problem with the chosen algorithm.')

    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='swarmlib v' + __version__,
        help='Show version and exit')
    parser.add_argument(
        '-d',
        '--dark',
        action='store_true',
        help='Enable dark mode.',
        default=False)
    parser.add_argument(
        '-i',
        '--interval',
        type=int,
        default=1000,
        help='Interval between two animation frames in ms (default 1000)')
    parser.add_argument(
        '-c',
        '--continuous',
        default=False,
        action='store_true',
        help='Enable the algorithm to run continuously (default off)')
    parser.add_argument(
        '-s',
        '--seed',
        default=None,
        type=int,
        help='Used to set the initial state of the random bit generator (default None)')
    parser.add_argument(
        '-l',
        '--log-level',
        default='info',
        choices=['debug', 'info', 'warning', 'error', 'critical'],
        help='Set the log level (default info)')

    sub_parsers = parser.add_subparsers(
        title='Commands',
        description='Valid commands',
        help='Choose the algorithm to execute')
    aco_parser(sub_parsers)
    firefly_parser(sub_parsers)
    cuckoo_parser(sub_parsers)
    pso_parser(sub_parsers)
    abc_parser(sub_parsers)
    gwo_parser(sub_parsers)
    args = vars(parser.parse_args())
    if args:
        log_level = args.pop('log_level')
        level = getattr(logging, log_level.upper())
        logging.basicConfig(
            format=f'%(asctime)s{" [%(threadName)-12.12s] [%(module)-12.12s]" if log_level == "debug" else ""} [%(levelname)-5.5s]  %(message)s',
            stream=sys.stdout,
            level=logging.INFO) # Set overall level to info
        logging.getLogger(__package__).setLevel(level) # Set the level for swarmlib components

        algorithm = args.pop('func')
        algorithm(args)
    else:
        parser.print_usage()


if __name__ == '__main__':
    run_swarm()
