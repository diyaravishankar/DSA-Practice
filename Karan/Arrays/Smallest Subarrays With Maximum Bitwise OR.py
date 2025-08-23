class Solution:
 def smallestSubarrays(self, nums):
  n=len(nums)
  answer=[0]*n
  or_to_len={}
  for i in range(n-1,-1,-1):
   new_or_to_len={nums[i]:1}
   for prev_or,length in or_to_len.items():
    combined_or=nums[i]|prev_or
    if combined_or not in new_or_to_len or new_or_to_len[combined_or]>length+1:
     new_or_to_len[combined_or]=length+1
   or_to_len=new_or_to_len
   max_or=max(or_to_len.keys())
   answer[i]=or_to_len[max_or]
  return answer