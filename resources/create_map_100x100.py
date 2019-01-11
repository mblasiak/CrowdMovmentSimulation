from model.environment.environment import direction_map
from model.environment.line import Point
from resources.handling.generating import create_txt_form_direction_map
n = 100
maze = [[0 for j in range(0, n)] for i in range(0, n)]

for i in range(0, 40):
    maze[i][96] = 1
    maze[i][97] = 1
    maze[i][98] = 1
    maze[i][99] = 1

for i in range(60, 100):
    maze[i][96] = 1
    maze[i][97] = 1
    maze[i][98] = 1
    maze[i][99] = 1

for i in range(0, 11):
    maze[i][50] = 1
    maze[i][51] = 1
    maze[i][52] = 1
    maze[i][47] = 1
    maze[i][48] = 1
    maze[i][49] = 1

for i in range(22, 33):
    maze[i][50] = 1
    maze[i][51] = 1
    maze[i][52] = 1
    maze[i][47] = 1
    maze[i][48] = 1
    maze[i][49] = 1

for i in range(44, 55):
    maze[i][50] = 1
    maze[i][51] = 1
    maze[i][52] = 1
    maze[i][47] = 1
    maze[i][48] = 1
    maze[i][49] = 1

for i in range(66, 77):
    maze[i][50] = 1
    maze[i][51] = 1
    maze[i][52] = 1
    maze[i][47] = 1
    maze[i][48] = 1
    maze[i][49] = 1

for i in range(88, 100):
    maze[i][50] = 1
    maze[i][51] = 1
    maze[i][52] = 1
    maze[i][47] = 1
    maze[i][48] = 1
    maze[i][49] = 1

exits = []
for i in range(40, 60):
    exits.append(Point(99, i))

exits = [Point(99, 50)]

print('Generating directions')
directions = direction_map(maze, exits, 1)
print('Directions generated')
print('Tralsating directions to txt')
create_txt_form_direction_map("ready/directios100x100yxWith1Exit.txt", directions)
print('Map has been saved')
