import unittest

import numpy as np

from src.agent.Agent import Agent
from src.environment.environment import direction_map
from src.environment.line import Point
from src.direction_map.DirectionMap import DirectionMap
from tests.tesing_tools.list_comparator.compare_lists import compare_lists
from tests.tesing_tools.print_list_diffrances.print_list_diffrances import print_2D_list_difrances


class AgentCollision(unittest.TestCase):

    def setUp(self):
        self.exit_point = (10, 10)
        self.start_pos = (5, 5)
        self.end_pos = self.exit_point
        self.max_step = 5
        self.front_collision = 2
        self.rear_collision = 1

        self.collisions = np.zeros((20, 20)).tolist()
        self.directions = direction_map(self.collisions, [Point(self.exit_point[0], self.exit_point[1])], self.max_step)

        self.direction_map = DirectionMap(self.directions)
        self.collision_map = self.collisions
        self.agent = Agent(self.start_pos, self.end_pos, self.max_step, self.front_collision, self.rear_collision,
                           self.direction_map, self.collision_map)

        self.expected_collisions = np.zeros((20, 20)).tolist()

    def test_no_agent_marks_on_start(self):
        self.assertTrue(compare_lists(self.expected_collisions, self.collisions))

    def test_agent_marks_something(self):
        self.agent.add_position_to_collision_map()
        self.assertFalse(compare_lists(self.expected_collisions, self.collisions))

    def test_agent_marks_propper_fields(self):
        self.agent.facing_angle = 0

        self.agent.add_position_to_collision_map()

        self.expected_collisions[4][5] = 1

        self.expected_collisions[5][3] = 1
        self.expected_collisions[5][4] = 1
        self.expected_collisions[5][5] = 1
        self.expected_collisions[5][6] = 1
        self.expected_collisions[5][7] = 1

        self.expected_collisions[6][5] = 1
        self.expected_collisions[6][6] = 1
        self.expected_collisions[6][4] = 1

        self.expected_collisions[7][5] = 1

        print_2D_list_difrances(self.expected_collisions, self.collisions)

        self.assertTrue(compare_lists(self.expected_collisions, self.collisions))

    def test_agent_marks_propper_fields_facing_up(self):
        self.agent.facing_angle = np.pi / 2

        self.agent.add_position_to_collision_map()

        self.expected_collisions[5][4] = 1
        self.expected_collisions[5][5] = 1
        self.expected_collisions[5][6] = 1
        self.expected_collisions[5][7] = 1

        self.expected_collisions[6][5] = 1
        self.expected_collisions[6][6] = 1

        self.expected_collisions[7][5] = 1

        self.expected_collisions[4][5] = 1
        self.expected_collisions[4][6] = 1

        self.expected_collisions[3][5] = 1

        print_2D_list_difrances(self.expected_collisions, self.collisions)

        self.assertTrue(compare_lists(self.expected_collisions, self.collisions))
