class Solution:
 def countGood(self, nums, k):
  from collections import defaultdict
  left=0
  total_pairs=0
  count=defaultdict(int)
  res=0
  for right in range(len(nums)):
   total_pairs+=count[nums[right]]
   count[nums[right]]+=1
   while total_pairs>=k:
    res+=len(nums)-right
    count[nums[left]]-=1
    total_pairs-=count[nums[left]]
    left+=1
  return res