from unittest import TestCase

from nearest_steakhouses import XNearestSteakHouses


class TestXNearestSteakHouses(TestCase):
    def test_get_x_nearest_steakhouses(self):
        all_locations = [[3, 4], [1, 1], [0, 0], [5, 6], [-1, -1], [-1, 0], [0, 1]]
        x = 4
        expected_nearest = {(0, 0), (0, 1), (-1, 0), (-1, -1)}
        expected_other = {(0, 0), (0, 1), (-1, 0), (1, 1)}
        x_nearest = {tuple(t) for t in XNearestSteakHouses.get_x_nearest_steakhouses(all_locations, x)}

        self.assertTrue(x_nearest == expected_nearest or x_nearest == expected_other)
        x = 5
        x_nearest = {tuple(t) for t in XNearestSteakHouses.get_x_nearest_steakhouses(all_locations, x)}
        self.assertTrue(x_nearest == (expected_other.union(expected_nearest)))
