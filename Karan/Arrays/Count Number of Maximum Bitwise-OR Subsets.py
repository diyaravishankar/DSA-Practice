class Solution:
 def countMaxOrSubsets(self,nums:list[int])->int:
  max_or,count=0,0
  def backtrack(i,cur_or):
   nonlocal count
   if i==len(nums):
    if cur_or==max_or:count+=1
    return
   backtrack(i+1,cur_or|nums[i])
   backtrack(i+1,cur_or)
  for num in nums:max_or|=num
  backtrack(0,0)
  return count