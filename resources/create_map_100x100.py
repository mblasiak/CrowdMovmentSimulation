from model.environment.environment import direction_map
from model.environment.line import Point
from resources.handling.generating import create_txt_form_direction_map
from resources.handling.reading import load_map_from_file

n = 100
maze = [[0 for j in range(0, n)] for i in range(0, n)]

"""generowannie glareia krakowska maze"""
# for x in range(55, 100):
#     for y in range(0, 34):
#         maze[y][x] = 1
#
# for y in range(51, 55):
#     for x in range(0, 30):
#         maze[x][y] = 1
# """next"""
#
# for i in range(34,40):
#     for j in range(55,57):
#         maze[i][j] = 1
#
# for i in range(46,52):
#     for j in range(55,57):
#         maze[i][j] = 1
#
# for i in range(58, 64):
#     for j in range(55, 57):
#         maze[i][j] = 1
#
# for i in range(70, 76):
#     for j in range(55, 57):
#         maze[i][j] = 1
#
# for i in range(82, 88):
#     for j in range(55, 57):
#         maze[i][j] = 1
#
# for i in range(94, 100):
#     for j in range(55, 57):
#         maze[i][j] = 1
#
# """next"""
# for i in range(40,46):
#     for j in range(62,64):
#         maze[i][j] = 1
#
# for i in range(52,58):
#     for j in range(62,64):
#         maze[i][j] = 1
#
# for i in range(64, 76):
#     for j in range(62, 64):
#         maze[i][j] = 1
#
# for i in range(82, 88):
#     for j in range(62, 64):
#         maze[i][j] = 1
#
# for i in range(94, 100):
#     for j in range(62, 64):
#         maze[i][j] = 1
#
# """next"""
# for i in range(48, 53):
#     for j in range(70, 76):
#         maze[j][i] = 1
#
# """next"""
# for i in range(94, 100):
#     for j in range(0,24):
#         maze[i][j] = 1
#
# """next"""
# for y in range(30, 64):
#     for x in range(7,21):
#         maze[y][x] = 1
#
# for y in range(0,11):
#     for x in range(7,21):
#         maze[y][x] = 1
#
# """next"""
# for i in range(66, 74):
#     for j in range(72, 90):
#         maze[i][j] = 1




exits = [Point(99, 90)]

mazeGK = load_map_from_file("ready/galeria_krakowska_maze100x100.txt")


print('Generating directions')
directions = direction_map(mazeGK, exits, 1)
print('Directions generated')
print('Tralsating directions to txt')
create_txt_form_direction_map("ready/GK_directionmap_four_100x100.txt", directions)
print('Map has been saved')
