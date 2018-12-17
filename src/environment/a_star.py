import bisect

from .line import Point

import numpy


def a_star(environment, start, end,d):  # (int[][], Point, Point)

    if len(environment) < start.y or len(environment[0]) < start.x or start.x < 0 or start.y < 0:
        raise PointOutOfEnvironmentRangeException(
            "Point (start: " + str(start) + ") out of environment range "
            + str(len(environment)) + "x" + str(len(environment[0])))
    if len(environment) < end.y or len(environment[0]) < end.x or end.x < 0 or end.y < 0:
        raise PointOutOfEnvironmentRangeException(
            "Point (end: " + str(end) + ") out of environment range "
            + str(len(environment)) + "x" + str(len(environment[0])))

    visited = []
    non_visited = []
    start_node = Node(None, start)
    non_visited.extend(get_neighbours(environment, start_node, end, []))
    non_visited.sort()

    while len(non_visited) > 0:
        lowest_cost_node = non_visited[0]
        if lowest_cost_node.cords == end:
            return reconstruct_path(lowest_cost_node)

        non_visited.remove(lowest_cost_node)
        visited.append(lowest_cost_node)

        neighbours = get_neighbours(environment, lowest_cost_node, end, visited)
        for node in neighbours:
            update = update_non_visited(node, non_visited)
            if update is not None:
                if update is True:
                    non_visited.append(node)
                    d[node.cords.y][node.cords.x] = 3
                else:
                    continue
            else:
                non_visited.append(node)
                d[node.cords.y][node.cords.x] = 3

        non_visited.sort()

    return False


def reconstruct_path(node):  # Point[] / Node
    path = []
    while node.parent is not None:
        path.append(node.cords)
        node = node.parent
    path.append(node.cords)
    path.reverse()
    return path


def already_visited(cords, nodes):  # Point, Node[])
    for node in nodes:
        if cords == node.cords:
            return True
    return False


def get_neighbours(environment, node, end, visited):  # Node[] / (Node, Point)
    """ get all the node correct neighbours """

    neighbours_cords = [
        Point(-1, -1), Point(0, -1), Point(1, -1),
        Point(-1, 0),                Point(1, 0),
        Point(-1, 1),  Point(0, 1),  Point(1, 1),
    ]

    environment_x_range = len(environment[0])
    environment_y_range = len(environment)

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

        # check if the cord is out of environment range
        if cords.x >= environment_x_range or cords.x < 0 or cords.y >= environment_y_range or cords.y < 0:
            continue

        # check if this cord is an obstacle (1 mean it is)
        if environment[cords.y][cords.x] == 1:
            continue

        # check if this cords have been already visited
        if already_visited(cords, visited):
            continue

        neighbour = Node(node, cords)
        neighbour.g_cost = node.g_cost + (numpy.sqrt(2) if diagonal_node else 1)
        neighbour.h_cost = diagonal_distance_heuristics(cords, end)

        # check if already same cords was seen, if yes and if new node is better remove old
        # for seen_node in non_visited:
        #     if node.cords == seen_node.cords:
        #         if node <= seen_node:
        #             non_visited.remove(seen_node)
        #         else:
        #             continue

        neighbours_nodes.append(neighbour)

    return neighbours_nodes


def update_non_visited(node, non_visited):  # (Node, Node[])
    for seen_node in non_visited:
        if node.cords == seen_node.cords:
            if node <= seen_node:
                non_visited.remove(seen_node)
                return True
            else:
                return False
    return None


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


class PointOutOfEnvironmentRangeException(Exception):
    def __init__(self, message):
        super(PointOutOfEnvironmentRangeException, self).__init__(message)