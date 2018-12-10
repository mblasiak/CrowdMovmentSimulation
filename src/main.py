import time

from environment.astar import diagonal_distance_heuristics, a_star
from environment.a_star import astar
from environment.environment import map_environment, get_obstacle_line_horizon, get_obstacle_line_vertical, \
    direction_map
from environment.line import Point, Line
from environment.astar import Node, get_neighbours

import numpy

maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

n=100

d = [[0 for j in range(0, n)] for i in range(0, n)]

for i in range(0, 25):
    j = i
    for j in range(0, j):
        d[i][j] = 1

print(a_star(maze, Point(0, 0), Point(2,2)))

# print(d)
#
#
# print(get_obstacle_line_horizon(maze))
# print(get_obstacle_line_vertical(maze))
#
# p1 = Point(0, 0)
# p2 = Point(6, 0)
#
# p3 = Point(4, 0)
#
# l1 = Line(p1, p2)
# l2 = Line(p3, p3)

# for ele in map_environment(maze, [(9, 1)]):
#     print(ele)


#
# print(astar(d, (0, 0), (91,91)))
#
# for ele in direction_map(d, [(50, 1), (50, 2), (50, 3)], 3):
#     print(ele)

parent = Node(None, Point(0, 0))
node = Node(parent, Point(1, 1))
end = Point(3, 3)
node.g_cost = numpy.sqrt(2)
print(get_neighbours(node, end))

node.h_cost=1

nod2 = Node(None, Point(1, 1))
nod2.g_cost = numpy.sqrt(2)
nod2.h_cost = 1

nod3 = Node(None, Point(1, 1))
nod3.g_cost = 14
nod3.h_cost = numpy.sqrt(2)

nod4 = Node(None, Point(1, 1))
nod4.g_cost = 14
nod4.h_cost = 2*numpy.sqrt(2)

l = [nod4, node, nod3, nod2]
print(l)

l.sort()
print(l)
