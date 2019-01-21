from copy import deepcopy
from random import randint

import model.navigator.navigator as nav
from model.agent.Agent import ExitReached
from model.environment.environment_enum import Env


class Agent:
    id = 0

    def __init__(self, start_position: (int, int), end_position: [(int, int)], gradient_maps,
                 collision_map: [[(int, int)]], which_gradient_map=0, bound_size=2):
        self.start = start_position
        self.end = end_position
        self.current_pos = self.start
        self.front_collision_size = bound_size
        self.direction_map = gradient_maps[which_gradient_map]
        self.collision_map = collision_map
        self.facing_angle = nav.get_angle_of_direction_between_points(self.current_pos, end_position[0])

        self.all_gradients = gradient_maps

        self.value_threshold = 10
        self.value = self.value_threshold

        self.gradient_space_size = 4

        self.update_gradient(self.value)

        self.id = randint(0, 1000)

        self.anger = 0

    def update_facing_angle(self, new_pos):
        self.facing_angle = nav.get_angle_of_direction_between_points(self.current_pos, new_pos)

    def get_available_moves(self):
        available_spots = []

        for y in range(self.current_pos[0]-1, self.current_pos[0]+2):
            for x in range(self.current_pos[1]-1, self.current_pos[1]+2):

                # If this point is current point we skip
                if y == self.current_pos[0] and x == self.current_pos[1]:
                    continue

                # If we out of range we skip
                if y >= len(self.collision_map) or x >= len(self.collision_map[0]) or \
                        y <= 0 or x <= 0:
                    continue

                if self.direction_map[y][x] == Env.OBSTACLE or self.direction_map[y][x] == Env.EXIT:
                    continue

                # if spot has lower gradient value then the current_pos we add it
                if self.direction_map[y][x] < self.direction_map[self.current_pos[0]][self.current_pos[1]]:
                    # we create list of ( gradient_value, (y, x) )
                    available_spots.append((self.direction_map[y][x], (y, x)))

        available_spots.sort()

        return available_spots

    def get_best_move(self, available_spots: [(int, (int, int))]):

        if len(available_spots) == 0:
            return None

        for i in range(0, len(available_spots)):
            a_y, a_x = available_spots[i][1]
            if self.collision_map[a_y][a_x] == 0:
                return available_spots[i][1]

        return None

    def block_point(self, position):
        self.collision_map[position[0]][position[1]] = 1

    def unblock_point(self, position):
        self.collision_map[position[0]][position[1]] = 0

    def update_gradient(self, value):
        for y in range(-self.gradient_space_size, self.gradient_space_size + 1):
            for x in range(-self.gradient_space_size, self.gradient_space_size + 1):

                local_y = self.current_pos[0] + y
                local_x = self.current_pos[1] + x

                if y >= 5 or y <= -5 or x >= 5 or x <= -5:
                    tmp_value = int(value/5)
                elif y == 4 or y == -4 or x == 4 or x == -4:
                    tmp_value = int(value/4)
                elif y == 3 or y == -3 or x == 3 or x == -3:
                    tmp_value = int(value/3)
                elif y == 2 or y == -2 or x == 2 or x == -2:
                    tmp_value = int(value/2)
                else:
                    tmp_value = value

                # If we this is current spot we double value here
                if local_y == self.current_pos[0] and local_x == self.current_pos[1]:
                    for i in range(0, len(self.all_gradients)):
                        self.all_gradients[i][local_y][local_x] += tmp_value*2
                    continue

                # If we out of range we skip
                if local_y >= len(self.collision_map) or local_x >= len(self.collision_map[0]) or \
                        local_y <= 0 or local_x <= 0:
                    continue

                # If spot is obstacle or exit we skip
                if self.direction_map[local_y][local_x] == Env.EXIT or \
                        self.direction_map[local_y][local_x] == Env.OBSTACLE:
                    continue

                # Normal situation
                for i in range(0, len(self.all_gradients)):
                    self.all_gradients[i][local_y][local_x] += tmp_value * 2

    def move(self):

        available_positions = self.get_available_moves()

        best_pos = self.get_best_move(available_positions)

        if best_pos is None:
            print("agnet blocked")
            # self.value += self.value
            # self.update_gradient(self.value)
            return 0

        self.unblock_point(self.current_pos)

        if best_pos == Env.EXIT or self.direction_map[best_pos[0]][best_pos[1]] < 65:
            self.update_gradient(-self.value)
            raise ExitReached

        self.update_facing_angle(best_pos)

        self.update_gradient(-self.value)

        self.current_pos = best_pos
        self.block_point(self.current_pos)

        self.update_gradient(self.value)

        return 0


