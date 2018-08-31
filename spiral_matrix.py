# https://leetcode.com/problems/spiral-matrix/description/


class SpiralMatrix:
    @staticmethod
    def spiral_order(matrix: [int]):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        result = []
        if matrix is []:
            return result

        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            for i in range(top + 1, bottom):
                result.append(matrix[i][right])
            if top < bottom:
                for j in reversed(range(left, right + 1)):
                    result.append(matrix[bottom][j])
            if left < right:
                for i in reversed(range(top + 1, bottom)):
                    result.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return result
