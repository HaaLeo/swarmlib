# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------


def _swap_2opt(route, i, k):
    """
    swaps the endpoints of two edges by reversing a section of nodes,
        ideally to eliminate crossovers
    returns the new route created with a the 2-opt swap
    route - route to apply 2-opt
    i - start index of the portion of the route to be reversed
    k - index of last node in portion of route to be reversed
    pre: 0 <= i < (len(route) - 1) and i < k < len(route)
    post: length of the new route must match length of the given route
    """
    assert i >= 0
    assert i < (len(route) - 1)
    assert k > i
    assert k < len(route)
    new_route = route[0:i]
    new_route.extend(reversed(route[i:k + 1]))
    new_route.extend(route[k+1:])
    assert len(new_route) == len(route)
    return new_route


def run_2opt(route, edge_distance_func):
    """
    improves an existing route using the 2-opt swap
    best path found will differ depending of the start node of the list of nodes
        representing the input tour
    returns the best path found
    route - route to improve
    """
    best_route = route
    best_distance = _route_distance(route, edge_distance_func)
    for i in range(1, len(best_route) - 1):
        for k in range(i+1, len(best_route) - 1):
            new_route = _swap_2opt(best_route, i, k)
            new_distance = _route_distance(new_route, edge_distance_func)
            if new_distance < best_distance:
                best_distance = new_distance
                best_route = new_route

    assert len(best_route) == len(route)
    return best_route, best_distance


def _route_distance(route, edge_distance_func):
    distance = 0.
    for idx in range(len(route) - 1):
        distance += edge_distance_func((route[idx], route[idx+1]))

    return distance
