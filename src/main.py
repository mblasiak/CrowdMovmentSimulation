from environment.a_star import astar
from environment.environment import map_environment, get_obstacle_line_horizon, get_obstacle_line_vertical, \
    direction_map
from environment.line import Point, Line

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


print(get_obstacle_line_horizon(maze))
print(get_obstacle_line_vertical(maze))

p1 = Point(0, 0)
p2 = Point(6, 0)

p3 = Point(4, 0)

l1 = Line(p1, p2)
l2 = Line(p3, p3)

for ele in map_environment(maze, [(9, 1)]):
    print(ele)

for ele in direction_map(maze, [Point(1, 9), Point(2, 9)], 3):
    print(ele)
