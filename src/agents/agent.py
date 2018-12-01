import numpy as np

from environment import a_star


class Agent:
    start_position = None
    end_position = None
    max_step = 1
    front_collision_size = None
    rear_collision_size = None
    direction_map = None
    free_space_map = None

    def __init__(self, start_position, end_postion, max_step, front_collison_size, rear_collision_size, directions_map,
                 free_space_map):
        self.start = start_position
        self.end = end_postion
        self.max_step = max_step
        self.front_collision_size = front_collison_size
        self.rear_collision_size = rear_collision_size
        self.direction_map = directions_map

    def get_prefered_direction(self):
        pass

    def get_avaialbe_moves(self):
        pass

    def get_move_price(self):
        pass

    def get_best_move(self):
        pass

    def update_collision_map(self):
        pass

    def clear_last_postionion_from_collision_map(self):
        pass

    def addd_new_position_to_collision_map(self):
        pass

    def move(self):
        pass



    def check_if_finish(self):
        if self.end == self.start:
            return True
        else:
            return False
