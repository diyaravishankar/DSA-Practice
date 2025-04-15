class Solution:
 def threeSumClosest(self, nums, target):
  nums.sort()
  n=len(nums)
  res=nums[0]+nums[1]+nums[2]
  for i in range(n-2):
   l=i+1
   r=n-1
   while l<r:
    s=nums[i]+nums[l]+nums[r]
    if abs(s-target)<abs(res-target):res=s
    if s<target:l+=1
    else:r-=1
  return res