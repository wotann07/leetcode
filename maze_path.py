from sys import maxsize


class MazePath:
    _num_cols = 0
    _num_rows = 0
    _lot = []

    @staticmethod
    def _is_valid_move(x: int, y: int, visited: []):
        return MazePath._num_cols > x >= 0 and MazePath._num_rows > y >= 0 and MazePath._lot[y][x] and not \
            visited[y][x]

    @staticmethod
    def _is_destination(x: int, y: int):
        return MazePath._lot[y][x] == 9

    @staticmethod
    def _get_path_from_here(x: int, y: int, visited: [], min_distance, distance):
        # base case
        if MazePath._is_destination(x, y):
            return min(min_distance, distance)
        else:
            visited[y][x] = 1

            # move down
            if MazePath._is_valid_move(x, y + 1, visited):
                min_distance = MazePath._get_path_from_here(x, y + 1, visited, min_distance, distance + 1)

            # move up
            if MazePath._is_valid_move(x, y - 1, visited):
                min_distance = MazePath._get_path_from_here(x, y - 1, visited, min_distance, distance + 1)

            # move left
            if MazePath._is_valid_move(x - 1, y, visited):
                min_distance = MazePath._get_path_from_here(x - 1, y, visited, min_distance, distance + 1)

            # move right
            if MazePath._is_valid_move(x + 1, y, visited):
                min_distance = MazePath._get_path_from_here(x + 1, y, visited, min_distance, distance + 1)

        visited[y][x] = 0
        return min_distance

    @staticmethod
    def get_shortest_path(lot: []):
        MazePath._lot = lot
        if len(MazePath._lot) < 1:
            return -1
        else:
            MazePath._num_cols = len(MazePath._lot[0])
            MazePath._num_rows = len(MazePath._lot)

            return MazePath._get_path_from_here(0, 0, [[0] * MazePath._num_cols for _ in range(MazePath._num_rows)],
                                                maxsize, 0)
