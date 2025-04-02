class Solution:
 def maximumTripletValue(self, nums):
  n=len(nums)
  max_value=0
  for i in range(n-2):
   for j in range(i+1,n-1):
    for k in range(j+1,n):
     max_value=max(max_value,(nums[i]-nums[j])*nums[k])
  return max_value