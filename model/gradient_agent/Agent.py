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

    def update_facing_angle(self, new_pos):
        self.facing_angle = nav.get_angle_of_direction_between_points(self.current_pos, new_pos)

    def get_available_moves(self):
        available_points = []

        for y in range(self.current_pos[0]-1, self.current_pos[0]+2):
            for x in range(self.current_pos[1]-1, self.current_pos[1]+2):
                if y == self.current_pos[0] and x == self.current_pos[1]:
                    continue

                if y >= len(self.collision_map) or x >= len(self.collision_map[0]):
                    continue

                if self.collision_map[y][x] == 0:
                    if self.direction_map[y][x] < self.direction_map[self.current_pos[0]][self.current_pos[1]]:
                        available_points.append((self.direction_map[y][x], (y, x)))

        available_points.sort()
        for i in range(0, len(available_points)):
            available_points[i] = available_points[i][1]

        return available_points

    def get_best_move(self, available_positions):

        for position in available_positions:
            if self.collision_map[position[0]][position[1]] == 0:
                return position

        return None

    def block_point(self, position):
        self.collision_map[position[0]][position[1]] = 1

    def unblock(self, position):
        self.collision_map[position[0]][position[1]] = 0

    def move(self):

        self.unblock(self.current_pos)
        available_positions = self.get_available_moves()

        best_pos = self.get_best_move(available_positions)

        if best_pos is None:
            self.block_point(self.current_pos)
            return 0

        if best_pos == Env.EXIT:
            return 1

        self.update_facing_angle(best_pos)
        self.current_pos = best_pos
        self.block_point(self.current_pos)

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
