from copy import deepcopy

from model.environment.environment_enum import Env
from resources.handling.reading import load_direction_from_file

import numpy


def gradient(direction_map_txt: str, ):
    """ Its supposed to return gradient map with ..."""
    direction_map = load_direction_from_file(direction_map_txt)

    gradient_map = deepcopy(direction_map)

    source = (50, 110)

    for y in range(0, len(direction_map)):
        for x in range(0, len(direction_map[y])):

            # Check if we already updated gradient map in [y][x]
            if gradient_map[y][x] != direction_map[y][x]:
                continue

            # If obstacle we skip
            if direction_map[y][x] == Env.OBSTACLE or direction_map[y][x] == Env.EXIT:
                continue

            point1 = (y, x)
            point2 = direction_map[y][x]
            gradient_map[y][x] = numpy.rad2deg(numpy.arctan2((point2[0]-point1[0]), (point2[1]-point1[1])))

            source_angel = numpy.rad2deg(numpy.arctan2((source[0]-point1[0]), (source[1]-point1[1])))

            gradient_map[y][x] = source_angel


    return gradient_map


def gradient_from_direction_map(direction_map_txt: str):
    direction_map = load_direction_from_file(direction_map_txt)

    gradient_map = deepcopy(direction_map)

    for y in range(0, len(direction_map)):
        for x in range(0, len(direction_map[y])):

            # Check if we already updated gradient map in [y][x]
            if gradient_map[y][x] != direction_map[y][x]:
                continue

            # If obstacle we skip
            if direction_map[y][x] == Env.OBSTACLE:
                continue

            position = direction_map[y][x]
            distance = 0
            while position != Env.EXIT:
                distance += 1
                position = direction_map[position[0]][position[1]]

            gradient_map[y][x] = distance
            position = direction_map[y][x]
            while position != Env.EXIT:
                distance -= 1
                gradient_map[position[0]][position[1]] = distance
                position = direction_map[position[0]][position[1]]

    return gradient_map





for ele in gradient("C:\\Users\\piotr\\Desktop\\CrowdSim\\resources/ready/directios100x100yx.txt"):
    print(ele)
