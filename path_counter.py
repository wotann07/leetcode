class PathCounter:
    @staticmethod
    def _get_pos_val(maze: [], row: int, column: int):
        return maze[row][column] if PathCounter._is_valid(maze, row, column) else 0

    @staticmethod
    def _is_valid(maze: [], row: int, column: int):
        """
        - This method only checks boundaries and 0's
        :return: True if valid, False otherwise
        """
        return 0 <= row < len(maze) and 0 <= column < len(maze[0]) and maze[row][column]

    @staticmethod
    def _count_paths_dp_helper(maze: []):
        """
        - Solution using iterative dynamic programming approach
        :param maze:
        :return: The number of possible paths from given location
        """
        # Do not need to check last row (gets rid of unnecessary validation)
        for row in range(len(maze) - 2, -1, -1):
            for column in range(len(maze[0]) - 1, -1, -1):
                if maze[row][column]:
                    maze[row][column] = PathCounter._get_pos_val(maze, row + 1, column) + \
                                        PathCounter._get_pos_val(maze, row, column + 1)

        return maze[0][0]

    @staticmethod
    def _count_paths_recursive_helper(maze: [], count_dict: {}, row: int, column: int):
        """
        - Recursive with memoization (equivalent to visited in shortest path)
        :return: The number of possible paths from given location
        """
        if row == len(maze) - 1 and column == len(maze[0]) - 1:
            return 1
        elif not PathCounter._is_valid(maze, row, column):
            return 0
        else:
            curr_count = count_dict.get((row, column))
            if not curr_count:
                curr_count = PathCounter._count_paths_recursive_helper(maze, count_dict, row + 1, column) + \
                             PathCounter._count_paths_recursive_helper(maze, count_dict, row, column + 1)
                count_dict[(row, column)] = curr_count

            return curr_count

    @staticmethod
    def count_paths(maze: []):
        """
        - Valid moves are right and down
        - Counts the paths from 0, 0 to (len(maze[0]), len(maze))
        - Obstacles defined by 0's in the maze
        - Viable paths defined by 1's

        :param maze: Maze of 0's and 1's
        :return: The number of possible paths from start to end in the given maze
        """
        _ = PathCounter._count_paths_dp_helper(maze)
        return PathCounter._count_paths_recursive_helper(maze, {}, 0, 0)
