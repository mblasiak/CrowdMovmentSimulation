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

        self.start = start_position
        self.end = end_position
        self.current_pos = self.start
        self.max_step = max_step

        self.front_collision_size = front_collision_size
        self.rear_collision_size = rear_collision_size
        self.direction_map = directions_map
        self.collision_map = collision_map
        self.current_facing_angle = directions_map.get_angle(self.current_pos)

    def update_facing_angle(self):
        self.current_facing_angle = self.direction_map.get_angle(self.current_pos)

    def get_available_moves(self):
        available_points = []
        (a_x, a_y) = self.current_pos

        for x in range(a_x - self.max_step, a_x + self.max_step):
            for y in range(a_y - self.max_step, a_y + self.max_step):
                distance = nav.get_distance_beteween_points(self.current_pos, (x, y))
                angle = nav.get_angle_of_direction_between_points(self.current_pos, (x, y))
                if distance <= self.max_step and abs(angle - self.current_facing_angle) <= self.forward_move_angle / 2:
                    available_points.append((x, y))

        return available_points

    def get_move_price(self, pos: (int, int)) -> float:
        move_angle = nav.get_angle_of_direction_between_points(self.current_pos, pos)
        move_step_lenght = nav.get_distance_beteween_points(self.current_pos, pos)
        desired_angle = self.direction_map.get_angle(self.current_pos)
        desired_step = self.direction_map.get_step_size(self.current_pos)

        return move_step_lenght / desired_step * self.speed_keeping_preference \
               + move_angle / desired_angle * self.direction_keeping_preference

    def get_best_move(self, moves):

        desired_move = self.direction_map.get_direction(self.current_pos)

        if self.collision_map[desired_move[0]][desired_move[1]] == 0:
            return desired_move

        if len(moves) == 0:
            return self.current_pos
        # TODO Refactor code under

        maxi = moves[0]
        max_price = 0
        for move in moves:
            current_price = self.get_move_price(move)
            if current_price > max_price:
                max_price = current_price
                maxi = move

        if (max_price < 0.1):
            return self.current_pos
        return move

    def update_collision_map(self, value):
        current_x, current_y = self.current_pos
        # update map only in neighbourhood of position
        front_collision = self.front_collision_size
        rear_collision = self.rear_collision_size
        for x in range(current_x - front_collision, current_x + front_collision):

            for y in range(current_y - front_collision, current_y + front_collision):

                distance = nav.get_distance_beteween_points(self.current_pos, (x, y))
                angle = nav.get_angle_of_direction_between_points(self.current_pos, (x, y))

                # Mark field if is in range and doesnt exceed angle diffrence from facing angle

                if distance <= front_collision and abs(
                        angle - self.current_facing_angle) <= np.pi / 2:
                    mark_location((x, y), self.collision_map, value)

                if distance <= rear_collision and abs(
                        angle - self.current_facing_angle) >= np.pi:
                    mark_location((x, y), self.collision_map, value)

    def clear_position_to_collision_map(self):
        self.update_collision_map(1)

    def add_position_to_collision_map(self):
        self.update_collision_map(-1)

    def move(self):
        print("{}--->".format(self.current_pos), end="")
        available_positions = self.get_available_moves()
        print(available_positions)
        best_pos = self.get_best_move(available_positions)
        self.clear_position_to_collision_map()
        self.current_pos = best_pos
        self.add_position_to_collision_map()
        self.update_facing_angle()
        print("{}".format(self.current_pos))

    def check_if_finish_has_been_reached(self):

        if self.end == self.current_pos:
            return True
        else:
            return False
