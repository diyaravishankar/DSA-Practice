class Solution:
 def partitionArray(self, nums, k):
  nums.sort()
  count = 0
  i = 0
  n = len(nums)
  while i < n:
   start = nums[i]
   while i < n and nums[i] - start <= k:
    i += 1
   count += 1
  return count