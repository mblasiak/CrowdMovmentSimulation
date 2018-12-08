import copy

from src.environment.environment_enum import Env
from src.environment.a_star import astar
from src.environment.line import Point, Line


def direction_map(environment, exit_points, step_size):
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
                fastest_paths = []
                for point in exit_points:
                    fastest_paths.append(astar(environment, (y, x), (point.y, point.x)))

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
                        possible_step = step_size
                        possible_step_is_correct = True
                        while possible_step >= 1:
                            if i+possible_step < len(shortest_path):
                                point_to_go = Point(shortest_path[i + possible_step][1], shortest_path[i + possible_step][0])
                            else:
                                last_index = len(shortest_path)-1
                                point_to_go = Point(shortest_path[last_index][1], shortest_path[last_index][0])
                                possible_step = last_index - i

                            line = Line(Point(current_x, current_y), point_to_go)
                            for line_obstacle in obstacles:
                                if line.intersect(line_obstacle):
                                    possible_step -= 1
                                    possible_step_is_correct = False
                                    break
                                else:
                                    possible_step_is_correct = True
                            if possible_step_is_correct is True:
                                x_l = shortest_path[i + possible_step][1]
                                y_l = shortest_path[i + possible_step][0]
                                direction_point = Point(x_l, y_l)
                                mapped_environment[current_y][current_x] = (x_l,y_l)
                                break
    return mapped_environment


def get_obstacle_line_vertical(environment):
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


def get_obstacle_line_horizon(environment):
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
        if path[i][1] != path[i-1][1] and path[i][0] != path[i-1][0]:
            distance += 14  # approximation of sqrt(2) * 10 (*10 so it's integer(14) not float(1,4))
        else:
            distance += 10
    return distance
