class Solution:
 def minCapability(self, nums, k):
  def can_rob_with_capability(cap):
   count = i = 0
   while i < len(nums):
    if nums[i] <= cap:
     count += 1
     i += 1
    i += 1
   return count >= k
  left, right = min(nums), max(nums)
  while left < right:
   mid = (left + right) // 2
   if can_rob_with_capability(mid):
    right = mid
   else:
    left = mid + 1
  return left