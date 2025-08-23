class Solution:
 def countMaxOrSubsets(self, nums):
  max_or = 0
  for num in nums:
   max_or |= num
  self.count = 0
  def backtrack(index, curr_or):
   if index == len(nums):
    if curr_or == max_or:
     self.count += 1
    return
   backtrack(index + 1, curr_or | nums[index])
   backtrack(index + 1, curr_or)
  backtrack(0, 0)
  return self.count