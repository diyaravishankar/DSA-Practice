class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] and i and j:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                res += matrix[i][j]
        return res