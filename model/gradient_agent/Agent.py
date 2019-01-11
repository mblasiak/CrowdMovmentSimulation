from random import randint

from model.direction_map import DirectionMap
import model.navigator.navigator as nav
from model.environment.environment_enum import Env
from model.gradient.gradient_map import gradient_from_direction_map
from resources.handling.reading import load_map_from_file


class Agent:
    def __init__(self, start_position: (int, int), end_position: [(int, int)], gradient_map,
                 collision_map: [[(int, int)]], bound_size=2):
        self.start = start_position
        self.end = end_position
        self.current_pos = self.start
        self.front_collision_size = bound_size
        self.direction_map = gradient_map
        self.collision_map = collision_map
        self.facing_angle = nav.get_angle_of_direction_between_points(self.current_pos, end_position[0])

        self.value = 10

        self.update_gradient(self.value)

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

                # If spot is free and if spot has lower gradient value then the current_pos we add it
                if self.collision_map[y][x] == 0:
                    if self.direction_map[y][x] < self.direction_map[self.current_pos[0]][self.current_pos[1]]:
                        # we create list of ( gradient_value, (y, x) )
                        available_spots.append((self.direction_map[y][x], (y, x)))

        available_spots.sort()
        # for i in range(0, len(available_spots)):
        #     available_spots[i] = available_spots[i][1]

        return available_spots

    def get_best_move(self, available_spots: [(int, (int, int))]):

        if len(available_spots) == 0:
            return None

        lowest_gradient_value = available_spots[0][0]

        lowest_gradient_spots = []
        rest_spots = []

        for spot in available_spots:
            if self.collision_map[spot[1][0]][spot[1][1]] == 0:
                if spot[0] == lowest_gradient_value:
                    lowest_gradient_spots.append(spot[1])
                else:
                    rest_spots.append(spot[1])

        if len(lowest_gradient_spots) != 0:
            for spot in lowest_gradient_spots:
                if spot[0] == self.current_pos[0] or spot[1] == self.current_pos[1]:
                    return spot
            random = randint(0, len(lowest_gradient_spots)-1)
            return lowest_gradient_spots[random]

        elif len(rest_spots) != 0:
            random = randint(0, len(rest_spots)-1)
            return rest_spots[random]

    def block_point(self, position):
        self.collision_map[position[0]][position[1]] = 1

    def unblock_point(self, position):
        self.collision_map[position[0]][position[1]] = 0

    def update_gradient(self, value):
        for y in range(self.current_pos[0]-1, self.current_pos[0]+2):
            for x in range(self.current_pos[1]-1, self.current_pos[1]+2):

                if y == self.current_pos[0] and x == self.current_pos[1]:
                    self.direction_map[y][x] += 2*value

                # If we out of range we skip
                if y >= len(self.collision_map) or x >= len(self.collision_map[0]) or \
                        y <= 0 or x <= 0:
                    continue

                if self.direction_map[y][x] == Env.EXIT or self.direction_map[y][x] == Env.OBSTACLE:
                    continue

                self.direction_map[y][x] += value

    def move(self):

        self.unblock_point(self.current_pos)
        available_positions = self.get_available_moves()

        best_pos = self.get_best_move(available_positions)

        if best_pos is None:
            self.block_point(self.current_pos)
            self.value += self.value
            self.update_gradient(self.value)
            return 0

        if best_pos == Env.EXIT or self.direction_map[best_pos[0]][best_pos[1]] == 0 or best_pos[1] > 96:
            self.update_gradient(-self.value)
            return 1


        self.update_facing_angle(best_pos)

        self.update_gradient(-self.value)

        self.current_pos = best_pos
        self.block_point(self.current_pos)
        self.value = 10
        self.update_gradient(self.value)


        return 0


#
#
# gradient_map = gradient_from_direction_map("C:\\Users\\piotr\\Desktop\\CrowdSim\\resources/ready/directios100x100yx.txt")
#
# maze = load_map_from_file("C:\\Users\\piotr\\Desktop\\CrowdSim\\resources\\ready\\dobry_maze100na100.txt")
#
# agent = Agent((4, 4), list(zip(range(40, 60), [99] * 20)), gradient_map, maze)
#
# print(agent.get_available_moves())
