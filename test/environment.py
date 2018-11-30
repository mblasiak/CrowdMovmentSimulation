import unittest

from src.environment.environment import path_distance


class TestDistanceCountingMethod(unittest.TestCase):

    def test_two_ele(self):
        self.assertEqual(path_distance([(1, 1), (1, 2)]), 10)

    def test_one_ele(self):
        self.assertEqual(path_distance([(1, 1)]), 0)

    def test_zero_ele(self):
        self.assertEqual(path_distance([]), 0)


if __name__ == '__main__':
    unittest.main()
