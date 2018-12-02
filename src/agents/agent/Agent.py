import numpy as np

import src.agents.navigation.navigator.navigator as nav
from src.agents.navigation.direction_map.DirectionMap import DirectionMap
from src.collisions.collision_map_tools import mark_location_as_taken


class Agent:
    def __init__(self, start_position, end_position, max_step, front_collision_size, rear_collision_size,
                 directions_map: DirectionMap(),
                 collision_map):

        self.start = start_position
        self.end = end_position
        self.current_pos = self.start
        self.max_step = max_step

        self.front_collision_size = front_collision_size
        self.rear_collision_size = rear_collision_size
        self.direction_map = directions_map
        self.collision_map = collision_map
        self.current_facing_angle = directions_map.get_desired__direction_angle(self.current_pos)

    def update_facing_angle(self):
        self.current_facing_angle = self.direction_map.get_desired__direction_angle(self.current_pos)

    def get_available_moves(self):
        pass

    def get_move_price(self):
        pass

    def get_best_move(self):
        pass

    def update_collision_map(self, value):
        current_x, current_y = self.current_pos
        # update map only in neighbourhood of position
        for x in range(current_x - self.front_collision_size, current_x + self.front_collision_size):
            for y in range(current_y - self.front_collision_size, current_y + self.front_collision_size):
                distnce_to_point = nav.get_distance_beteween_points(self.current_pos, (x, y))
                angle_of_point_direction = nav.get_angle_of_direction_between_points(self.current_pos, (x, y))
                # Mark field if is in range and doesnt exceed angle diffrence from facing angle
                if distnce_to_point <= self.front_collision_size and abs(
                        angle_of_point_direction - self.current_facing_angle) <= np.pi / 2:
                    mark_location_as_taken((x, y), self.collision_map, value)

                if distnce_to_point <= self.rear_collision_size and abs(
                        angle_of_point_direction - self.current_facing_angle) >= np.pi:
                    mark_location_as_taken((x, y), self.collision_map, value)

    def clear_position_to_collision_map(self):
        self.update_collision_map(1)

    def add_position_to_collision_map(self):
        self.update_collision_map(-1)

    def move(self):
        pass

    def check_if_finish_has_been_reached(self):

        if self.end == self.current_pos:
            return True
        else:
            return False
