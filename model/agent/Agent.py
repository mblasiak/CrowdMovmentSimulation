import numpy as np

import model.navigator.navigator as nav
from model.direction_map import DirectionMap
from model.collisions.collision_map_tools import mark_location
from model.environment.environment_enum import Env
from model.environment.a_star import astar


class Agent:
    def __init__(self, start_position: (int, int), end_position: [(int, int)], directions_map: DirectionMap,
                 collision_map: [[(int, int)]], bound_size=2, max_step=1, ):

        self.start = start_position
        self.end = end_position
        self.current_pos = self.start
        self.max_step = max_step
        self.front_collision_size = bound_size
        self.direction_map = directions_map
        self.collision_map = collision_map
        self.facing_angle = directions_map.get_angle(self.current_pos)

        self.forward_move_angle = np.pi * (8 / 10)
        self.speed_keeping_preference = 0.6
        self.direction_keeping_preference = 1 - self.speed_keeping_preference
        self.minimal_move_price = 0.05

        self.release_space()

    def update_facing_angle(self, new_pos):
        self.facing_angle = nav.get_angle_of_direction_between_points(self.current_pos, new_pos)

    def get_available_moves(self):
        available_points = []
        (a_y, a_x) = self.current_pos

        for x in range(a_x - self.max_step, a_x + self.max_step):
            for y in range(a_y - self.max_step, a_y + self.max_step):

                if y >= len(self.collision_map) or x >= len(self.collision_map[y]):
                    continue
                if self.collision_map[y][x] == 0:
                    distance = nav.get_distance_beteween_points(self.current_pos, (y, x))
                    angle = nav.get_angle_of_direction_between_points(self.current_pos, (y, x))
                    if distance <= self.max_step and abs(angle - self.facing_angle) <= self.forward_move_angle / 2:
                        available_points.append((y, x))

        return available_points

    def get_move_price(self, pos: (int, int)) -> float:

        if self.direction_map.direction_map[pos[0]][pos[1]] == Env.EXIT:
            return 256
        move_angle = nav.get_angle_of_direction_between_points(self.current_pos, pos)
        move_step_length = nav.get_distance_beteween_points(self.current_pos, pos)

        desired_angle = self.direction_map.get_angle(self.current_pos)
        desired_step = self.direction_map.get_step_size(self.current_pos)

        price = (move_step_length % desired_step) / desired_step * self.speed_keeping_preference \
                + (2 * np.pi - (desired_angle - move_angle)) / (2 * np.pi) * self.direction_keeping_preference
        return price

    def get_best_move(self, moves):

        closest_exit = min(self.end, key=lambda exit: nav.get_distance_beteween_points(self.current_pos, exit))
        desireds = astar(self.collision_map, closest_exit, self.current_pos)
        desireds = desireds[::-1]
        if (len(desireds) < 1):
            return self.current_pos
        desired_move = desireds[1].y, desireds[1].x

        if self.collision_map[desired_move[0]][desired_move[1]] == 0:
            return desired_move

        if len(moves) == 0:
            print('Had no ther moves')
            return self.current_pos

        maxi = max(moves, key=lambda z: self.get_move_price(z))
        if self.get_move_price(maxi) >= self.minimal_move_price:
            print('Used alternative move')
            return maxi

        else:
            print('Used current pos')
            return self.current_pos

    def update_collisions(self, value):
        current_y, current_x = self.current_pos
        collision = self.front_collision_size
        for x in range(current_x - collision, current_x + collision + 1):
            for y in range(current_y - collision, current_y + collision + 1):
                mark_location((y, x), self.collision_map, value)

    def block_space(self):
        self.update_collisions(-1)

    def release_space(self):
        self.update_collisions(1)

    def move(self):
        self.block_space()
        available_positions = self.get_available_moves()

        best_pos = self.get_best_move(available_positions)

        if self.finished_reached(best_pos):
            return 1
        self.update_facing_angle(best_pos)
        self.current_pos = best_pos
        self.release_space()

        return 0

    def finished_reached(self, pos):
        if pos in self.end:
            return True
        else:
            return False
