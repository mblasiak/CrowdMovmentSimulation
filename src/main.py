import time

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

for ele in direction_map(maze, [(9, 1)], 3):
    print(ele)

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

#f= open("direction_map.txt", "w+")


points = []
for i in range(40,60):
    points.append(Point(99, i))

for tab in direction_map(d, points, 1):
    print(tab)
    #for ele in tab:
        #f.write(str(ele))
        #f.write(' ')
    #f.write('\n')
t2 = time.time()
print(str(t2 - t1))

