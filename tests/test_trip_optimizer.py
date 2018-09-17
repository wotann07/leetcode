from unittest import TestCase

from trip_optimizer import TripOptimizer


class TestTripOptimizer(TestCase):
    def test_get_optimal_routes(self):
        forward_trips = [[1, 3000], [2, 400], [3, 7000], [4, 12000]]
        return_trips = [[1, 2000], [2, 7000], [3, 2500]]
        max_distance = 14000
        expected = [[3, 2], [4, 1]]

        self.assertTrue(expected == TripOptimizer.get_optimal_routes(max_distance, forward_trips, return_trips))
        max_distance = 100
        expected = []
        self.assertTrue(expected == TripOptimizer.get_optimal_routes(max_distance, forward_trips, return_trips))
