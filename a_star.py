import math
from functools import total_ordering
from heapq import heappush, heappop, heapify

from breadth_first_search import Node


@total_ordering
class HeuristicNode(Node):
    dst = None

    def __init__(self, x=0, y=0, parent=None):
        Node.__init__(self, x, y, 0, parent, '')
        self.g = (parent.g + 1) if parent else 0
        self.h = self._simple_manhattan_heuristic()
        self.f = self.g + self.h

    def _simple_manhattan_heuristic(self):
        return math.fabs(HeuristicNode.dst[0] - self.x) + math.fabs(HeuristicNode.dst[1] - self.y)

    def set_new_parent(self, parent):
        self.__init__(self.x, self.y, parent)

    def get_neighbours(self, maze: []):
        is_valid_move = lambda n: 0 <= n.x < len(maze[0]) and 0 <= n.y < len(maze) and maze[n.y][n.x]
        return [n for n in [HeuristicNode(self.x + 1, self.y, self), HeuristicNode(self.x - 1, self.y, self),
                            HeuristicNode(self.x, self.y + 1, self), HeuristicNode(self.x, self.y - 1, self)] if
                is_valid_move(n)]

    def __eq__(self, other):
        if isinstance(other, HeuristicNode):
            return super(HeuristicNode, self).__eq__(other)
        elif isinstance(other, tuple):
            if len(other) == 2:
                return other[0] == self.x and other[1] == self.y
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, HeuristicNode):
            return self.f < other.f or (self.f == other.f and self.g < other.g)
        else:
            return NotImplemented


class AStar:
    @staticmethod
    def get_path(node: Node):
        path = []
        n = node
        while n is not None:
            path.append((n.x, n.y))
            n = n.parent

        path.reverse()
        return path

    @staticmethod
    def find_path_a_star(end_pos: tuple, maze: [], start_pos=(0, 0)):
        open_heap = []  # it is a min heap
        open_set = {}
        closed_set = {}

        HeuristicNode.dst = end_pos
        start = HeuristicNode(start_pos[0], start_pos[1])
        heappush(open_heap, start)
        open_set[(start.x, start.y)] = start

        while len(open_heap) > 0:
            current = heappop(open_heap)
            del open_set[(current.x, current.y)]
            if current == end_pos:
                return AStar.get_path(current)
            closed_set[(current.x, current.y)] = current
            for t in map(lambda pos: ((pos.x, pos.y), pos), current.get_neighbours(maze)):
                if closed_set.get(t[0]) is None:
                    open_neighbour = open_set.get(t[0])
                    if open_neighbour is None:
                        heappush(open_heap, t[-1])
                        open_set[(t[-1].x, t[-1].y)] = t[-1]
                    else:
                        if t[-1].g < open_neighbour.g:
                            open_neighbour.set_new_parent(t[-1].parent)
                            heapify(open_heap)
        return False
