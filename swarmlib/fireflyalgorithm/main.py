
def _run_firefly_algorithm():
    pass


def configure_parser(sub_parsers):
    """
    Get the argument parser for the ant colony optimization algorithm
    """

    parser = sub_parsers.add_parser(
        'fireflies',
        description='Solving an minimation problem using the firefly algorithm',
        help='Firefly algorithm for minimation problem')

    parser.set_defaults(func=_run_firefly_algorithm)
