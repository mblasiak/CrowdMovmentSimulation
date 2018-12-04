import numpy as np


class DirectionMap:

    # TODO Maybe refactor code to stop faterfall execution of methods
    # TODO especially reading from direction_map

    def __init__(self, direction_map: [[(int, int)]]):
        self.direction_map = direction_map

    def get_next_desired_location(self, current_pos: (int, int)):
        (current_x, current_y) = current_pos
        return self.direction_map[current_x][current_y]

    def get_desired__direction(self, current_pos: (int, int)):
        return tuple(np.subtract(self.get_next_desired_location(current_pos),current_pos))

    def get_desired_step_size(self, current_pos: (int, int)):
        (desired_x, desired_y) = self.get_desired__direction(current_pos)
        # Return distance between current location and desired location
        return (desired_x ** 2 + desired_y ** 2) ** 0.5

    def get_desired__direction_angle(self, current_pos: (int, int)):
        # y/x=tg
        # alpha=arctan(y/x)

        (desired_x, desired_y) = self.get_desired__direction(current_pos)

        # if x=0 cant use arctg
        if desired_x == 0:
            if y >= 0:
                return np.pi / 2
            else:
                return np.pi * 1.5

        return np.arctan(desired_y / desired_x)
