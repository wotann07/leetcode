from collections import deque
from sys import maxsize


class Node:
    def __init__(self, x=0, y=0, distance=0, parent=None, move=None):
        if parent:
            self.distance = parent.distance + 1
            if move is 'up':
                self.x = parent.x
                self.y = parent.y - 1
            elif move is 'down':
                self.x = parent.x
                self.y = parent.y + 1
            elif move is 'left':
                self.x = parent.x - 1
                self.y = parent.y
            elif move is 'right':
                self.x = parent.x + 1
                self.y = parent.y
            else:
                self.x, self.y = x, y
        else:
            self.x, self.y, self.distance = x, y, distance
        self.parent = parent


class BFS:
    @staticmethod
    def get_path(node: Node):
        path = []
        n = node
        while n is not None:
            path.append(n)
            n = n.parent

        path.reverse()
        return path

    @staticmethod
    def find_path_breadth_first(maze: [], start_pos=(0, 0), end_value=9):
        q_open = deque([])
        visited = [[False] * len(maze[0]) for _ in range(len(maze))]
        min_distance = maxsize

        curr_node = Node(start_pos[0], start_pos[1])
        q_open.append(curr_node)
        visited[curr_node.y][curr_node.x] = True

        while len(q_open) > 0:
            curr_node = q_open.popleft()
            if maze[curr_node.y][curr_node.x] == end_value:
                min_distance = curr_node.distance
                break

            is_valid_move = lambda n: 0 <= n.x < len(maze[0]) and 0 <= n.y < len(maze) and maze[n.y][n.x] and not \
                visited[n.y][n.x]

            for node in [Node(parent=curr_node, move='up'),
                         Node(parent=curr_node, move='down'),
                         Node(parent=curr_node, move='left'),
                         Node(parent=curr_node, move='right')]:
                if is_valid_move(node):
                    q_open.append(node)
                    visited[node.y][node.x] = True
        if curr_node and min_distance != maxsize:
            print(str([(node.x, node.y) for node in BFS.get_path(curr_node)]).strip('[]'))
        return min_distance
