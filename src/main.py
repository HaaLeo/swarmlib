import logging
import sys
from ACOProblem import ACOProblem

logging.basicConfig(
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    stream=sys.stdout,
    level=logging.DEBUG)

if __name__ == '__main__':
    """The main entry point. Currently used for debug purpose."""
    logger = logging.getLogger(__name__)
    logger.debug('Hello World')
    problem = ACOProblem('resources/burma14.tsp', 1)
    problem.solve()
    i = 6
