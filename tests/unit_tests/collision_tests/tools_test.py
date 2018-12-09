import copy
import unittest

import numpy as np

from src.collisions.collision_map_tools import mark_location_as_taken


class TestMarking(unittest.TestCase):

    def setUp(self):

        self.collision_map = np.zeros((100, 100)).tolist()

    def test_mark_position(self):
        desired_result =copy.deepcopy(self.collision_map)

        desired_result[2][2] = 1

        mark_location_as_taken((2, 2), self.collision_map, 1)

        self.assertTrue(self.compare_elements(desired_result, self.collision_map))

    def test_mark_far_position(self):
        desired_result = copy.deepcopy(self.collision_map)
        desired_result[35][88] = 1

        mark_location_as_taken((35, 88), self.collision_map, 1)

        self.assertTrue(self.compare_elements(desired_result,self.collision_map))

    def test_doesnt_allways_equal(self):
        desired_result = copy.deepcopy(self.collision_map)
        desired_result[35][88] = 1

        mark_location_as_taken((30, 88), self.collision_map, 1)

        self.assertFalse(self.compare_elements(desired_result,self.collision_map))

    def compare_elements(self, a, b):
        for x in range(0, len(a)):
            for y in range(0, len(a[1])):

                if (a[x][y]) != (b[x][y]):
                    return False

        return True
