import logging
import sys
from aco_problem import ACOProblem

logging.basicConfig(
    format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s',
    stream=sys.stdout,
    level=logging.INFO)

if __name__ == '__main__':
<<<<<<< HEAD
    LOGGER = logging.getLogger(__name__)
    LOGGER.debug('Hello World')
    PROBLEM = ACOProblem('resources/burma14.tsp', 10, num_iterations=100, plot_interval=10)
    if PROBLEM.solve():
        PROBLEM.show_result()
=======
    """The main entry point. Currently used for debug purpose."""
    logger = logging.getLogger(__name__)
    logger.debug('Hello World')
    problem = ACOProblem('resources/burma14.tsp', 28)
    problem.solve()
    problem.show_result(True)
>>>>>>> 85ab989f81bf74556ae06b3f7d4cd413905ec958
