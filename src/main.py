import logging
import sys
from aco_problem import ACOProblem

logging.basicConfig(
    format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s',
    stream=sys.stdout,
    level=logging.INFO)

if __name__ == '__main__':
    LOGGER = logging.getLogger(__name__)
    LOGGER.debug('Hello World')
    PROBLEM = ACOProblem('resources/burma14.tsp', 14, num_iterations=10, plot_interval=1)
    if PROBLEM.solve():
        PROBLEM.show_result()
