import numpy as np

class Agent:

    def __init__(self, start_position, end_postion, max_step, front_collison_size, rear_collision_size, directions_map,
                 collision_map):

        self.start = start_position
        self.end = end_postion
        self.current_pos = self.start
        self.max_step = max_step

        self.front_collision_size = front_collison_size
        self.rear_collision_size = rear_collision_size
        self.direction_map = directions_map
        self.collision_map = collision_map
        self.map_x_size = len(directions_map)
        self.map_y_size = len(directions_map[0])

    def get_next_desired_location(self):
        (current_x, current_y) = self.current_pos
        return self.direction_map[current_x][current_y]

    def get_desired__direction(self):
        return self.get_next_desired_location() - self.current_pos

    def get_desired_step_size(self):
        (desired_x, desired_y) = self.get_desired__direction()

        # Return distance beetwen current location and desired location
        return (desired_x ** 2 + desired_y ** 2) ** 0.5

    def get_desired__direction_angle(self):
        # y/x=tg
        # alpha=arctg(y/x)

        (desired_x, desired_y) = self.get_desired__direction()

        # if x=0 cant use arctg
        if (desired_x == 0):
            if (y >= 0):
                return np.pi / 2
            else:
                return np.pi * 1.5

        return np.arctan(desired_y / desired_x)

    def get_avaialbe_moves(self):

        pass

    def get_move_price(self):
        pass

    def get_best_move(self):
        pass

    def update_collision_map(self):

        pass

    def clear_from_collision_map(self):
        pass

    def add_position_to_collision_map(self):

        pass

    def move(self):
        pass

    def check_if_finish(self):

        if self.end == self.current_pos:
            return True
        else:
            return False
