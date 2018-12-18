import numpy as np

import src.navigator.navigator as nav
from src.direction_map import DirectionMap
from src.collisions.collision_map_tools import mark_location


class Agent:
    def __init__(self, start_position: (int, int), end_position: (int, int), max_step: int, front_collision_size: float,
                 rear_collision_size: float,
                 directions_map: DirectionMap,
                 collision_map: [[(int, int)]]):

        self.forward_move_angle = np.pi * (8 / 10)
        self.speed_keeping_preference = 0.6
        self.direction_keeping_preference = 1 - self.speed_keeping_preference
        self.minmal_move_price = 0.05

        self.start = start_position
        self.end = end_position
        self.current_pos = self.start
        self.max_step = max_step

        self.front_collision_size = front_collision_size
        self.rear_collision_size = rear_collision_size
        self.direction_map = directions_map
        self.collision_map = collision_map
        self.facing_angle = directions_map.get_angle(self.current_pos)
        self.move_counter = 0
        print("KOKO")
        print( self.direction_map.get_next_position((45,44)))

    def update_facing_angle(self):
        self.facing_angle = self.direction_map.get_angle(self.current_pos)

    def get_available_moves(self):
        available_points = []
        (a_x, a_y) = self.current_pos

        for x in range(a_x - self.max_step, a_x + self.max_step):
            for y in range(a_y - self.max_step, a_y + self.max_step):

                if x >= len(self.collision_map) or y >= len(self.collision_map[x]):
                    continue
                distance = nav.get_distance_beteween_points(self.current_pos, (x, y))
                angle = nav.get_angle_of_direction_between_points(self.current_pos, (x, y))
                if distance <= self.max_step and abs(angle - self.facing_angle) <= self.forward_move_angle / 2:
                    available_points.append((x, y))

        return available_points

    def get_move_price(self, pos: (int, int)) -> float:

        move_angle = nav.get_angle_of_direction_between_points(self.current_pos, pos)
        move_step_length = nav.get_distance_beteween_points(self.current_pos, pos)

        desired_angle = self.direction_map.get_angle(self.current_pos)
        desired_step = self.direction_map.get_step_size(self.current_pos)

        price = desired_step / move_step_length * self.speed_keeping_preference \
                + move_angle / desired_angle * self.direction_keeping_preference
        return price

    def get_best_move(self, moves):
        desired_move = self.direction_map.get_next_position(self.current_pos)

        if self.collision_map[desired_move[0]][desired_move[1]] == 0:
            print("Chose desired move")

            return desired_move

        if len(moves) == 0:
            return self.current_pos

        maxi = max(moves, key=lambda z: self.get_move_price(z))
        if self.get_move_price(maxi) >= self.minmal_move_price:
            return maxi
        else:
            return self.current_pos

    def update_collision_map(self, value):
        current_x, current_y = self.current_pos
        front_collision = self.front_collision_size
        rear_collision = self.rear_collision_size

        for x in range(current_x - front_collision, current_x + front_collision + 1):
            for y in range(current_y - front_collision, current_y + front_collision + 1):

                distance = nav.get_distance_beteween_points(self.current_pos, (x, y))
                angle = nav.get_angle_of_direction_between_points(self.current_pos, (x, y))
                angle_diff = abs(angle - self.facing_angle)

                # Mark field if is in range and doesnt exceed angle diffrence from facing angle
                if np.pi / 2 < angle_diff < (np.pi * 3 / 2):
                    if distance <= rear_collision:
                        mark_location((x, y), self.collision_map, value)

                else:
                    if distance <= front_collision:
                        mark_location((x, y), self.collision_map, value)

    def clear_position_to_collision_map(self):
        self.update_collision_map(-1)

    def add_position_to_collision_map(self):
        self.update_collision_map(1)

    def move(self):
        if self.move_counter == 0:
            self.add_position_to_collision_map()

        self.clear_position_to_collision_map()
        available_positions = self.get_available_moves()

        best_pos = self.get_best_move(available_positions)

        self.current_pos = best_pos
        self.update_facing_angle()
        self.add_position_to_collision_map()


        if self.check_if_finish_has_been_reached():
            return 1

        self.move_counter = self.move_counter + 1
        return 0

    def check_if_finish_has_been_reached(self):

        if self.end == self.current_pos:
            return True
        else:
            return False
