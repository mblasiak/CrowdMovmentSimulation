import numpy as np


def get_direction_to_another_point(pos_1: (int, int), pos_2: (int, int)):
    return pos_2 - pos_1


def get_distance_beteween_points(pos_1: (int, int), pos_2: (int, int)):
    (desired_x, desired_y) = get_direction_to_another_point(pos_1, pos_2)
    return (desired_x ** 2 + desired_y ** 2) ** 0.5


def get_angle_of_direction_between_points(pos_1: (int, int), pos_2: (int, int)):
    # y/x=tg
    # alpha=arctan(y/x)
    (desired_x, desired_y) = get_direction_to_another_point(pos_1, pos_2)
    # if x=0 cant use arctg
    if desired_x == 0:
        if y >= 0:
            return np.pi / 2
        else:
            return np.pi * 1.5
    return np.arctan(desired_y / desired_x)
