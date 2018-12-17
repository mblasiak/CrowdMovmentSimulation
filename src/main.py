import copy
import time


from environment.a_star import diagonal_distance_heuristics, a_star
from environment.line import Point, Line
from environment.environment import direction_map

from environment.aaaa import astar

from environment.will import a_star as will


maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0]]

n=50

d = [[0 for j in range(0, n)] for i in range(0, n)]

for i in range(0, 10):
    d[i][25] = 1

for i in range(15, 50):
    d[i][25] = 1

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

d2 = copy.deepcopy(d)
d3 = copy.deepcopy(d)

"""   """
# t1 = time.time()
# for ele in direction_map(d, [Point(49, 20), Point(49, 21)], 1):
#     print(ele)
# # for y in range(0, len(d)):
# #     for x in range(0, len(d[0])):
# #         print(astar(d2, Point(x, y), Point(49,25)))
#
# t2 = time.time()
# print(str(t2 - t1))



# t1 = time.time()
# aa = astar(d2, Point(0,0), Point(49,25))
# print(aa)
# # for ele in direction_map(d, [Point(99, 49), Point(99, 48)], 2):
# #     print(ele)
# t2 = time.time()
# print(str(t2 - t1))
#
t1 = time.time()
will = a_star(d3, Point(5,5), Point(49,49), d3)
print(will)
# for ele in direction_map(d, [Point(99, 49), Point(99, 48)], 2):
#     print(ele)
t2 = time.time()
print(str(t2 - t1))


# print(aa[1])

maze2 = copy.deepcopy(maze)
import matplotlib.pyplot as plt


# for ele in aa:
#         d2[ele.y][ele.x] = 2
# # for i in maze:
# #         print(i)

# plt.imshow(d2)
#
# plt.show()


for ele in will:
        d3[ele.y][ele.x] = 2
# for i in maze:
#         print(i)

plt.imshow(d3)

plt.show()



