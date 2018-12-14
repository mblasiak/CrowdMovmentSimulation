import time


from environment.a_star import diagonal_distance_heuristics, a_star
from environment.line import Point, Line
from environment.environment import direction_map


maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]

n=100

d = [[0 for j in range(0, n)] for i in range(0, n)]

for i in range(0, 50):
    d[i][50] = 1

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
# for ele in direction_map(d, [Point(1, 9), Point(2, 9), Point(3, 9)], 1):
#     print(ele)
# print(a_star(d, Point(0,0), Point(99,99), d))
# e = t2-t1


#print(a_star(d, Point(0,0), Point(99,49)))

t1 = time.time()

for ele in direction_map(d, [Point(99, 49), Point(99, 48)], 2):
    print(ele)
t2 = time.time()
print(str(t2 - t1))




