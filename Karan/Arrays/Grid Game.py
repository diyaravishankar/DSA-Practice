class Solution:
 def gridGame(self, grid: List[List[int]]) -> int:
  n = len(grid[0])
  top = [0] * n
  bottom = [0] * n
  top[0] = grid[0][0]
  bottom[0] = grid[1][0]
  for i in range(1, n):
   top[i] = top[i-1] + grid[0][i]
   bottom[i] = bottom[i-1] + grid[1][i]
  res = float('inf')
  for i in range(n):
   top_remaining = top[n-1] - top[i] if i < n-1 else 0
   bottom_remaining = bottom[i-1] if i > 0 else 0
   res = min(res, max(top_remaining, bottom_remaining))
  return res