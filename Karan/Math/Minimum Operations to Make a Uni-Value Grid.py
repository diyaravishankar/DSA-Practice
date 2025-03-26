class Solution:
 def minOperations(self, grid, x):
  nums=[num for row in grid for num in row]
  nums.sort()
  median=nums[len(nums)//2]
  if any((num-median)%x for num in nums):return -1
  return sum(abs(num-median)//x for num in nums)