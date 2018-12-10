from .line import Point

import numpy


def a_star(environment, start, end):  # (int[][], Point, Point)
    visited = []
    non_visited = []
    start_node = Node(None, start)
    non_visited.extend(get_neighbours(start_node, end))
    non_visited.sort()

    while len(non_visited) > 0:
        lowest_cost_node = non_visited[0]
        if lowest_cost_node.cords == end:
            return reconstruct_path()

        non_visited.remove(lowest_cost_node)
        visited.append(lowest_cost_node)

        non_visited.extend(get_neighbours(lowest_cost_node, end))
        # TODO have to add sth to not double some neighbours (with out it works but not sure)
        non_visited.sort()

    return False


def reconstruct_path():
    return True


def already_visited(node, visited):  # (Node, Node[])
    for visited_node in visited:
        if node.cords == visited_node.cords:
            return True
    return False


def get_neighbours(node, end):  # (Node, Point)
    """ get all the node neighbours, without parent of the node"""

    neighbours_cords = [
        Point(-1, -1), Point(0, -1), Point(1, -1),
        Point(-1, 0),                Point(1, 0),
        Point(-1, 1),  Point(0, 1),  Point(1, 1),
    ]

    neighbours_nodes = []
    for cords in neighbours_cords:

        # if it is parent node we skip
        if node.parent is not None and cords+node.cords == node.parent.cords:
            continue

        # if we move vertically or horizontal we move 1, if diagonal sqrt(2)
        diagonal_node = True
        if cords.y == 0 or cords.x == 0:
            diagonal_node = False

        cords += node.cords

        neighbour = Node(node, cords)
        neighbour.g_cost = node.g_cost + (numpy.sqrt(2) if diagonal_node else 1)
        neighbour.h_cost = diagonal_distance_heuristics(cords, end)
        neighbours_nodes.append(neighbour)

    return neighbours_nodes


def diagonal_distance_heuristics(current, end):  # (Point, Point)
    """ we have to use different heuristic since we can move just in 8 direction, more info:
    http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html#diagonal-distance"""

    # d = 1
    d2 = numpy.sqrt(2)
    dx = numpy.abs(end.x - current.x)
    dy = numpy.abs(end.y - current.y)

    if dx > dy:
        return (dx - dy) + d2 * dy
    else:
        return (dy - dx) + d2 * dx


# TODO change compare (bad code)
class Node:
    def __init__(self, parent, cords):
        self.parent = parent
        self.cords = cords
        self.g_cost = 0  # cost from start to current
        self.h_cost = 0  # cost from current to end

    def f_cost(self):
        return self.g_cost+self.h_cost

    def __cmp__(self, other):
        if self.f_cost() > other.f_cost():
            return 1
        elif self.f_cost() < other.f_cost():
            return -1
        else:
            if self.h_cost > other.h_cost:
                return 1
            elif self.h_cost < other.h_cost:
                return -1
            else:
                return 0

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0

    def __ne__(self, other):
        return self.__cmp__(other) != 0

    def __repr__(self):
        return str(self.cords) + ", g=" + str(self.g_cost) + ", h=" + str(self.h_cost)
