from model.environment.environment import direction_map
from model.environment.line import Point
from resources.creator.DirectionMapToTxt import create_txt_form_direction_map
n = 100
d = [[0 for j in range(0, n)] for i in range(0, n)]

for i in range(0, 40):
    d[i][96] = 1
    d[i][97] = 1
    d[i][98] = 1
    d[i][99] = 1

for i in range(60, 100):
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

exits = []
for i in range(40, 60):
    exits.append(Point(99, i))

directions = direction_map(d, exits, 1)
create_txt_form_direction_map("ready/kupa.txt",directions)
