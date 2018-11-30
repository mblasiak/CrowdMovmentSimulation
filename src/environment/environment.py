import copy

from environment.environment_enum import Env
from environment.a_star import astar


def map_environment(environment, exit_points):
    """ Return mapped environment, each cord has next cord in 'fastest' path to exit """

    mapped_environment = copy.deepcopy(environment)
    for i in range(0, len(mapped_environment)):
        for j in range(0, len(mapped_environment[i])):
            if mapped_environment[i][j] == 1:
                mapped_environment[i][j] = Env.OBSTACLE
            else:
                mapped_environment[i][j] = None

    for y in range(0, len(environment)):
        for x in range(0, len(environment[y])):
            if environment[y][x] != 1:  # 1 mean there is obstacle
                if mapped_environment[y][x] is None:
                    fastest_paths = []
                    for point in exit_points:
                        fastest_paths.append(astar(environment, (y, x), point))

                    shortest_path = fastest_paths[0]
                    distance_of_shortest_path = path_distance(shortest_path)
                    for path in fastest_paths:
                        if distance_of_shortest_path > path_distance(path):
                            shortest_path = path
                            distance_of_shortest_path = path_distance(path)

                    for i in range(0, len(shortest_path)):
                        current_x = shortest_path[i][1]
                        current_y = shortest_path[i][0]
                        if i == len(shortest_path)-1:
                            mapped_environment[current_y][current_x] = Env.EXIT
                        else:
                            mapped_environment[current_y][current_x] = shortest_path[i+1]

    return mapped_environment


def path_distance(path):

    distance = 0
    for i in range(1, len(path)):
        if path[i][1] != path[i-1][1] and path[i][0] != path[i-1][0]:
            distance += 14  # approximation of sqrt(2) * 10 (*10 so it's integer(14) not float(1,4))
        else:
            distance += 10
    return distance
