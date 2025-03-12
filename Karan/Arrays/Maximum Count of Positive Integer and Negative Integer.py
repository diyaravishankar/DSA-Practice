from bisect import bisect_left
class Solution:
 def maximumCount(self, nums):
  neg_count = bisect_left(nums, 0)
  pos_count = len(nums) - bisect_left(nums, 1)
  return max(neg_count, pos_count)
sol = Solution()
print(sol.maximumCount([-2,-1,-1,1,2,3]))
print(sol.maximumCount([-3,-2,-1,0,0,1,2]))
print(sol.maximumCount([5,20,66,1314]))