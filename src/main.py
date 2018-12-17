import copy
import time


from environment.a_star import diagonal_distance_heuristics, a_star
from environment.line import Point, Line
from environment.environment import direction_map

from environment.aaaa import astar




maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

n=100

d = [[0 for j in range(0, n)] for i in range(0, n)]
#
# for i in range(0,70):
#     d[i][50] = 1
#     d[i][51] = 1
#     d[i][52] = 1
#     d[i][47] = 1
#     d[i][48] = 1
#     d[i][49] = 1
# #
# for i in range(40,100):
#     d[i][70] = 1
#     d[i][71] = 1
#     d[i][72] = 1
#     d[i][73] = 1
#     d[i][74] = 1
#     d[i][75] = 1
#
# for i in range(20,80):
#     d[i][30] = 1
#     d[i][31] = 1
#     d[i][32] = 1
#     d[i][33] = 1
#     d[i][34] = 1
#     d[i][35] = 1


for i in range(0, 40):
    d[i][96] = 1
    d[i][97] = 1
    d[i][98] = 1
    d[i][99] = 1

for i in range(60,100):
    d[i][96] = 1
    d[i][97] = 1
    d[i][98] = 1
    d[i][99] = 1

for i in range(0, 11):
    d[i][50] = 1
    d[i][51] = 1
    d[i][52] = 1
    d[i][47] = 1
    d[i][48] = 1
    d[i][49] = 1

for i in range(22, 33):
    d[i][50] = 1
    d[i][51] = 1
    d[i][52] = 1
    d[i][47] = 1
    d[i][48] = 1
    d[i][49] = 1

for i in range(44, 55):
    d[i][50] = 1
    d[i][51] = 1
    d[i][52] = 1
    d[i][47] = 1
    d[i][48] = 1
    d[i][49] = 1

for i in range(66, 77):
    d[i][50] = 1
    d[i][51] = 1
    d[i][52] = 1
    d[i][47] = 1
    d[i][48] = 1
    d[i][49] = 1

for i in range(88, 100):
    d[i][50] = 1
    d[i][51] = 1
    d[i][52] = 1
    d[i][47] = 1
    d[i][48] = 1
    d[i][49] = 1

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
f= open("direction_map.txt", "w+")
#
# for tab in d:
#     for ele in tab:
#         f.write(str(ele))
#         f.write(' ')
#     f.write('\n')


t1 = time.time()

points = []
for i in range(40,60):
    points.append(Point(99, i))

for tab in direction_map(d, points, 1):
    print(tab)
    for ele in tab:
        f.write(str(ele))
        f.write(' ')
    f.write('\n')
t2 = time.time()
print(str(t2 - t1))





#
# t1 = time.time()
# aa = astar(d2, Point(0,20), Point(99,44), d2)
# print(aa)
# # for ele in direction_map(d, [Point(99, 49), Point(99, 48)], 2):
# #     print(ele)
# t2 = time.time()
# print(str(t2 - t1))

# t1 = time.time()
# will = a_star(d, Point(0,23), Point(99,30), d)
# print(will)
# # for ele in direction_map(d, [Point(99, 49), Point(99, 48)], 2):
# #     print(ele)
# t2 = time.time()
# print(str(t2 - t1))


# print(aa[1])

maze2 = copy.deepcopy(maze)
import matplotlib.pyplot as plt


# for ele in will:
#         d[ele.y][ele.x] = 2
# # for i in maze:
# #         print(i)
#
# plt.imshow(d)
#
# plt.show()


# for ele in aa:
#         d2[ele.y][ele.x] = 2
# # for i in maze:
# #         print(i)
#
# plt.imshow(d2)
#
# plt.savefig('plot1.png')
#
# plt.show()





