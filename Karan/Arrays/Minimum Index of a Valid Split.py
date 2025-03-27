class Solution:
 def minimumIndex(self, nums):
  from collections import Counter
  count=Counter(nums)
  dom=max(count,key=count.get)
  left_count=0
  for i in range(len(nums)-1):
   if nums[i]==dom:left_count+=1
   if left_count*2>(i+1) and (count[dom]-left_count)*2>(len(nums)-i-1):return i
  return -1