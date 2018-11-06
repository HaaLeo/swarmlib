import logging
from threading import Thread

LOGGER = logging.getLogger(__name__)


class Ant(Thread):
    def __init__(self, start_node, graph):
        Thread.__init__(self)
        self.current_node = start_node
        self.next_node = None
        self.graph = graph

    def run(self):
        # Possible locations where the ant can got to from the current node.
        possible_locations = self.graph.get_connected_nodes(self.current_node)
        LOGGER.debug('Possible locations="%s"', possible_locations)

        self.next_node = 1 #TODO change
