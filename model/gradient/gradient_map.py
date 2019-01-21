from copy import deepcopy

from model.environment.environment_enum import Env
from resources.handling.reading import load_direction_from_file


def gradient_from_direction_map(direction_map_txt: str):
    """Returns gradient map based on distance counted from direction map"""
    direction_map = load_direction_from_file(direction_map_txt)

    # Make gradient map same size as direction map
    gradient_map = deepcopy(direction_map)

    # Main loop, loop through all the points
    for y in range(0, len(direction_map)):
        for x in range(0, len(direction_map[y])):

            # Check if we already updated gradient map in [y][x]
            if gradient_map[y][x] != direction_map[y][x]:
                continue

            # If obstacle we skip
            if direction_map[y][x] == Env.OBSTACLE:
                continue

            # Get current position
            position = direction_map[y][x]

            # Initialize distance variable for distance from the start point
            distance = 0


            # Loop till EXIT found so distance is full
            while position != Env.EXIT:

                # Get next position
                next_position = direction_map[position[0]][position[1]]

                if next_position == Env.EXIT:  # TODO its bad break exit, find better solution for this
                    break

                # Check if we move vertical (+10) or if diagonal (+14 (sqrt(2)*10))
                if position[0] == next_position[0] or position[1] == next_position[1]:
                    distance += 10
                else:
                    distance += 14

                position = next_position

            # Loop again and fill gradient map with correct distance
            gradient_map[y][x] = distance
            # Again get current position
            position = direction_map[y][x]
            while position != Env.EXIT:

                # Get next position
                next_position = direction_map[position[0]][position[1]]
                if next_position == Env.EXIT:
                    break

                # Check if we move vertical (-10) or if diagonal (-14 (sqrt(2)*10))
                if position[0] == next_position[0] or position[1] == next_position[1]:
                    distance -= 10
                else:
                    distance -= 14

                gradient_map[position[0]][position[1]] = distance
                position = next_position

    return gradient_map

