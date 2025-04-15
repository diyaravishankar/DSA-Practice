class Solution:
 def goodTriplets(self, nums1, nums2):
  n=len(nums1)
  pos1=[0]*n
  pos2=[0]*n
  for i in range(n):
   pos1[nums1[i]]=i
   pos2[nums2[i]]=i
  idx=[0]*n
  for i in range(n):
   idx[i]=pos2[nums1[i]]
  from bisect import bisect_left,insort
  left=[]
  right=[0]*n
  for i in range(n):
   p=bisect_left(left,idx[i])
   right[i]=p
   insort(left,idx[i])
  left=[]
  left_count=[0]*n
  for i in range(n-1,-1,-1):
   p=bisect_left(left,-idx[i])
   left_count[i]=p
   insort(left,-idx[i])
  res=0
  for i in range(n):
   res+=right[i]*left_count[i]
  return res