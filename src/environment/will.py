import numpy

from environment.line import Point


class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent, position):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return str(self.position)

    def __repr__(self):
        return str(self.position)


def a_star(environment, start, end, d):
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Main loop
    while len(open_list) > 0:

        ## Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the end point
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        #childredn
        children = []
        for new_position in [
            Point(-1, -1), Point(0, -1), Point(1, -1),
            Point(-1, 0),                Point(1, 0),
            Point(-1, 1),  Point(0, 1),  Point(1, 1),
        ]:
            # Get node position
            node_position = current_node.position + new_position

            # Make sure within range
            if node_position.y > (len(environment) - 1) or node_position.y < 0 or node_position.x > (len(environment[len(environment) - 1]) - 1) or node_position.x < 0:
                continue

            # Make sure walkable terrain
            if environment[node_position.y][node_position.x] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)
        # # Get neighbours
        # children = []
        # neighbours_cords = [
        #     Point(-1, -1), Point(0, -1), Point(1, -1),
        #     Point(-1, 0),                Point(1, 0),
        #     Point(-1, 1),  Point(0, 1),  Point(1, 1),
        # ]
        # # TODO
        # for new_position in [Point(0, -1), Point(0, 1), Point(-1, 0), Point(1, 0), Point(-1, -1), Point(-1, 1), Point(1, -1), Point(1, 1)]:
        #
        #     # Get the new cords
        #     node_position = current_node.position + new_position
        #
        #     # Check if the cord is out of environment range
        #     if node_position.x > (len(environment[0])-1) or node_position.x < 0 or node_position.y > (len(environment)-1) or node_position.y < 0:
        #         continue
        #
        #     # Check if this cord is an obstacle (1 mean it is)
        #     if environment[node_position.y][node_position.x] == 1:
        #         continue
        #
        #     neighbour = Node(current_node, node_position)
        #
        #     # if we move vertically or horizontal we move 1, if diagonal sqrt(2)
        #     """diagonal_node = True
        #     if cords.y == 0 or cords.x == 0:
        #         diagonal_node = False"""
        #
        #     children.append(neighbour)

        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = numpy.sqrt((child.position.y - end_node.position.y) ** 2) + ((child.position.x - end_node.position.x) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
            d[child.position.y][child.position.x] = 3

        # for child in children:
        #
        #     # TODO
        #     # Check if this cords have been already visited
        #     already_visited_flag = False
        #     for visited in visited_list:
        #         if visited == child:
        #             # already_visited_flag = True
        #             continue
        #     # # Skip if already visited
        #     # if already_visited_flag is True:
        #     #     continue
        #     # for visited in visited_list:
        #     #     if visited == neighbour:
        #     #         continue
        #
        #     # Create the f, g, and h values
        #     child.g = current_node.g + 1  # + (numpy.sqrt(2) if diagonal_node else 1)
        #     child.h = numpy.sqrt((child.position.y-end.y)**2 + (child.position.x-end.x)**2) #diagonal_distance_heuristics(neighbour.position, end)
        #     child.f = child.g + child.h
        #
        #     # Node is already in non visited list
        #     " here is a change "
        #     # already_in_non_visited = False
        #     # worst_then_different_node = False
        #     # for seen_node in open_list:
        #     #     if seen_node == child:
        #     #         # If it is we check if its better
        #     #         already_in_non_visited = True
        #     #
        #     #         if seen_node.g < child.g:
        #     #             worst_then_different_node = True
        #     #             break
        #     #         # And if it is better, we remove old one
        #     #         else:
        #     #             open_list.remove(seen_node)
        #     #             break
        #     # # Skip if it is worst then one of non_visited nodes
        #     # if already_in_non_visited is True:
        #     #     if worst_then_different_node is True:
        #     #         continue
        #     # for open_node in visited_list:
        #     #     if neighbour == open_node and neighbour.g > open_node.g:
        #     #         continue
        #     for open_node in open_list:
        #         if child == open_node and child.g > open_node.g:
        #             continue
        #
        #     open_list.append(child)
        #     d[child.position.y][child.position.x] = 3



def diagonal_distance_heuristics(current, end):  # (Point, Point)
    """We have to use different heuristic since we can move just in 8 direction, more info:
    http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html#diagonal-distance"""

    # d = 1
    d2 = numpy.sqrt(2)
    dx = numpy.abs(end.x - current.x)
    dy = numpy.abs(end.y - current.y)

    if dx > dy:
        return (dx - dy) + d2 * dy
    else:
        return (dy - dx) + d2 * dx