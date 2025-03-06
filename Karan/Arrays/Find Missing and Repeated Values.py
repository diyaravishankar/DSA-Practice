class Solution:
 def findMissingAndRepeatedValues(self, grid):
  n = len(grid)
  nums = [num for row in grid for num in row]
  num_set = set(nums)
  repeated = sum(nums) - sum(num_set)
  missing = sum(range(1, n * n + 1)) - sum(num_set)
  return [repeated, missing]
sol = Solution()
print(sol.findMissingAndRepeatedValues([[1,3],[2,2]]))
print(sol.findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))