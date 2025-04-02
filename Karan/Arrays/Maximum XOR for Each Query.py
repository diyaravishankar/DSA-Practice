class Solution:
 def getMaximumXor(self, nums, maximumBit):
  max_xor=(1<<maximumBit)-1
  xor_sum=0
  answer=[]
  for num in nums:
   xor_sum^=num
  for i in range(len(nums)):
   answer.append(xor_sum^max_xor)
   xor_sum^=nums[-1-i]
  return answer