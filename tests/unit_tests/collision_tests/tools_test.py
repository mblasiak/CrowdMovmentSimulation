import copy
import unittest

import numpy as np

from src.collisions.collision_map_tools import add_squere_obstacle, mark_location_as_taken, add_circle_obstacle


class TestMarking(unittest.TestCase):

    def setUp(self):
        self.collision_map = np.zeros((100, 100)).tolist()

    def test_mark_position(self):
        desired_result = copy.deepcopy(self.collision_map)

        desired_result[2][2] = 1

        mark_location_as_taken((2, 2), self.collision_map, 1)

        self.assertTrue(compare_elements(desired_result, self.collision_map))

    def test_mark_far_position(self):
        desired_result = copy.deepcopy(self.collision_map)
        desired_result[35][88] = 1

        mark_location_as_taken((35, 88), self.collision_map, 1)

        self.assertTrue(compare_elements(desired_result, self.collision_map))

    def test_doesnt_allways_equal(self):
        desired_result = copy.deepcopy(self.collision_map)
        desired_result[35][88] = 1

        mark_location_as_taken((30, 88), self.collision_map, 1)

        self.assertFalse(compare_elements(desired_result, self.collision_map))

    def test_return_true_when_marking_in_range(self):
        self.assertTrue(mark_location_as_taken((30, 88), self.collision_map, 1))

    def test_return_false_when_markoing_out_of_range(self):
        self.assertFalse(mark_location_as_taken((120, 99), self.collision_map, 1))

    def test_do_not_mark_when_out_of_range(self):
        desired_result = copy.deepcopy(self.collision_map)

        mark_location_as_taken((300, 88), self.collision_map, 1)

        self.assertTrue(compare_elements(desired_result, self.collision_map))


class ObstacleAdding(unittest.TestCase):

    def setUp(self):
        self.collision_map = np.zeros((100, 100)).tolist()

    def test_marking_squere(self):
        desired_result = copy.deepcopy(self.collision_map)

        desired_result[2][2] = 1
        desired_result[2][1] = 1
        desired_result[2][3] = 1

        desired_result[1][2] = 1
        desired_result[1][1] = 1
        desired_result[1][3] = 1

        desired_result[3][1] = 1
        desired_result[3][2] = 1
        desired_result[3][3] = 1

        add_squere_obstacle((2, 2), 2, self.collision_map, 1)

        self.assertTrue(compare_elements(desired_result, self.collision_map))

    def test_marking_circle(self):
        desired_result = copy.deepcopy(self.collision_map)

        desired_result[2][2] = 1
        desired_result[2][1] = 1
        desired_result[2][3] = 1

        desired_result[1][2] = 1

        desired_result[3][2] = 1

        add_circle_obstacle((2, 2), 1, self.collision_map, 1)
        self.assertTrue(compare_elements(desired_result, self.collision_map))


def compare_elements(a, b):
    for x in range(0, len(a)):
        for y in range(0, len(a[1])):

            if (a[x][y]) != (b[x][y]):
                return False

    return True
