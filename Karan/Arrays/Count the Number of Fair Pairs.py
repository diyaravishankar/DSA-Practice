from bisect import bisect_left, bisect_right
class Solution:
 def countFairPairs(self, nums, lower, upper):
  nums.sort()
  count = 0
  for i in range(len(nums)):
   left = bisect_left(nums, lower - nums[i], i + 1)
   right = bisect_right(nums, upper - nums[i], i + 1)
   count += right - left
  return count
sol = Solution()
print(sol.countFairPairs([0,1,7,4,4,5], 3, 6)) 
print(sol.countFairPairs([1,7,9,2,5], 11, 11)) 
print(sol.countFairPairs([3,5,7,9,11], 10, 15)) 