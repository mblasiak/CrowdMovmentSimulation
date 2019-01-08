import time

from environment.line import Point, Line
from environment.environment import direction_map


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


p1 = Point(0, 0)
p2 = Point(6, 0)

p3 = Point(4, 0)

l1 = Line(p1, p2)
l2 = Line(p3, p3)

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

t1 = time.time()

f= open("direction_map.txt", "w+")

points = []
for i in range(40,60):
    points.append(Point(99, i))

for tab in (direction_map(d, points, 1)):
    print(tab)
#     for p in tab:
#         f.write(str(p))
#         f.write(" ")
#     f.write("\n")
#
# f.close()




