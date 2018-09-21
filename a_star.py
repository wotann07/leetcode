import heapq

from breadth_first_search import Node


# TODO: FINISH A* IMPLEMENTATION
class HeuristicNode(Node):
    def __init__(self, g: int, h: int, f: int, x=0, y=0, distance=0, parent=None, move=''):
        Node.__init__(self, x, y, distance, parent, move)
        self.g = g
        self.h = h
        self.f = f


class AStar:
    @staticmethod
    def simple_manhattan_heuristic():
        raise Exception('IMPLEMENT ME')

    @staticmethod
    def find_path_a_star(end_pos: tuple, maze: [], start_pos=(0, 0), end_value=9):
        _ = end_pos, maze, start_pos, end_value
        min_heap = []
        # to be deleted
        heapq.heapify(min_heap)
        _ = min_heap
        pass
