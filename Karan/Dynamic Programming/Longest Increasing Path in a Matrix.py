class Solution:
  def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
    if not matrix: return 0
    m, n = len(matrix), len(matrix[0])
    from functools import lru_cache
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    @lru_cache(None)
    def dfs(x, y):
      val = matrix[x][y]
      res = 1
      for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > val:
          res = max(res, 1 + dfs(nx, ny))
      return res
    return max(dfs(i, j) for i in range(m) for j in range(n))