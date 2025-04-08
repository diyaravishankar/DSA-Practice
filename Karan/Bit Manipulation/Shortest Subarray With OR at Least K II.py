class Solution:
 def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
  from collections import deque
  n=len(nums)
  res=n+1
  ors=deque()
  for num in nums:
   new_ors=deque()
   new_ors.append((num,1))
   for val,length in ors:
    new_val=val|num
    if not new_ors or new_ors[-1][0]!=new_val:
     new_ors.append((new_val,length+1))
   ors=new_ors
   for val,length in ors:
    if val>=k:
     res=min(res,length)
     break
  return res if res<=n else -1