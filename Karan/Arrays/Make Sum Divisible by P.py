class Solution:
 def minSubarray(self,nums,p):
  total=sum(nums)
  remainder=total%p
  if remainder==0:
   return 0
  prefix={0:-1}
  prefix_sum=0
  min_len=float('inf')
  for i,num in enumerate(nums):
   prefix_sum=(prefix_sum+num)%p
   target=(prefix_sum-remainder)%p
   if target in prefix:
    min_len=min(min_len,i-prefix[target])
   prefix[prefix_sum]=i
  return min_len if min_len<len(nums) else -1