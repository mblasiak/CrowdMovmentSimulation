import copy
import numpy

from .environment_enum import Env

from .line import Point, Line

from .aaaa import astar


def direction_map(environment, exit_points, step_size):  # (Point,Env)[][] / (int[][], Point[], int)
    """ Return direction map with adjusted step_size"""
    mapped_environment = copy.deepcopy(environment)
    for i in range(0, len(mapped_environment)):
        for j in range(0, len(mapped_environment[i])):
            if mapped_environment[i][j] == 1:
                mapped_environment[i][j] = Env.OBSTACLE
            else:
                mapped_environment[i][j] = None

    obstacles = get_obstacle_line_horizon(environment) + get_obstacle_line_vertical(environment)

    for y in range(0, len(environment)):
        for x in range(0, len(environment[y])):
            if mapped_environment[y][x] is None:
                # TODO instead of counting a_star for each exit point we can choose best one with heuristic distance
                # TODO I done it but its not best solution,
                """ fastest_paths = [] """
                closest_point = exit_points[0]
                shortest_distance = diagonal_distance_heuristics(Point(x, y), closest_point)
                for point in exit_points:
                    distance = diagonal_distance_heuristics(Point(x,y), point)
                    if distance < shortest_distance:
                        shortest_distance = distance
                        closest_point = point
                    # fastest_paths.append(a_star(environment, Point(x, y), point))

                shortest_path = astar(environment, Point(x, y), closest_point)

                """ we can skip this since we are getting closest point earlier """
                # distance_of_shortest_path = path_distance(shortest_path)
                # for path in fastest_paths:
                #     if distance_of_shortest_path > path_distance(path):
                #         shortest_path = path
                #         distance_of_shortest_path = path_distance(path)
                # TODO end of TODO

                for i in range(0, len(shortest_path)):

                    current_x = shortest_path[i].x
                    current_y = shortest_path[i].y

                    #  check if it is pointless to continue mapping
                    if mapped_environment[current_y][current_x] is not None:
                        break
                    if i == len(shortest_path) - 1:
                        mapped_environment[current_y][current_x] = Env.EXIT
                    else:
                        mapped_environment[current_y][current_x] = shortest_path[i+1]

                    # if i == len(shortest_path)-1:
                    #     mapped_environment[current_y][current_x] = Env.EXIT
                    # else:
                    #     possible_step = step_size
                    #     possible_step_is_correct = True
                    #     while possible_step >= 1:
                    #         if i+possible_step < len(shortest_path):
                    #             point_to_go = Point(shortest_path[i + possible_step].x, shortest_path[i + possible_step].y)
                    #         else:
                    #             last_index = len(shortest_path)-1
                    #             point_to_go = Point(shortest_path[last_index].x, shortest_path[last_index].y)
                    #             possible_step = last_index - i
                    #
                    #         # TODO we can skipp it if step is 1 or 2
                    #         line = Line(Point(current_x, current_y), point_to_go)
                    #         for line_obstacle in obstacles:
                    #             if line.intersect(line_obstacle):
                    #                 possible_step -= 1
                    #                 possible_step_is_correct = False
                    #                 break
                    #             else:
                    #                 possible_step_is_correct = True
                    #         if possible_step_is_correct is True:
                    #             mapped_environment[current_y][current_x] = point_to_go
                    #             break
    return mapped_environment


def get_obstacle_line_vertical(environment):  # Line[] / int[][]
    is_line_started = False
    lines = []
    for i in range(0, len(environment[0])):
        line_vertical = Line(None, None)
        for j in range(0, len(environment)):
            if environment[j][i] == 1 and is_line_started is False:
                is_line_started = True
                line_vertical.point_start = Point(i, j)
                line_vertical.point_end = Point(i, j)
            elif environment[j][i] == 1 and is_line_started is True:
                line_vertical.point_end = Point(i, j)
            elif environment[j][i] == 0 and is_line_started is True:
                lines.append(line_vertical)
                is_line_started = False
    return lines


def get_obstacle_line_horizon(environment):  # Line[] / int[][]
    is_line_started = False
    lines = []
    for i in range(0, len(environment)):
        line_horizon = Line(None, None)
        for j in range(0, len(environment[i])):
            if environment[i][j] == 1 and is_line_started is False:
                is_line_started = True
                line_horizon.point_start = Point(j, i)
                line_horizon.point_end = Point(j, i)
            elif environment[i][j] == 1 and is_line_started is True:
                line_horizon.point_end = Point(j, i)
            elif environment[i][j] == 0 and is_line_started is True:
                lines.append(line_horizon)
                is_line_started = False
    return lines


def path_distance(path):
    distance = 0
    for i in range(1, len(path)):
        if path[i].x != path[i-1].x and path[i].y != path[i-1].y:
            distance += numpy.sqrt(2)
        else:
            distance += 1
    return distance
