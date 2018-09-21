from unittest import TestCase

from breadth_first_search import BFS
from maze_path import MazePath


class TestMazePath(TestCase):
    def test_get_shortest_path(self):
        maze = [[0, 1, 0, 1, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 9, 0],
                [0, 1, 1, 1, 0],
                [1] * 5]

        self.assertEqual(7, BFS.find_path_breadth_first(maze))
        self.assertEqual(7, MazePath.get_shortest_path(maze))
