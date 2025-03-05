class Solution:
 def coloredCells(self, n: int) -> int:
  return 2 * n * (n - 1) + 1
sol = Solution()
print(sol.coloredCells(1))
print(sol.coloredCells(2))
print(sol.coloredCells(3))
print(sol.coloredCells(4))