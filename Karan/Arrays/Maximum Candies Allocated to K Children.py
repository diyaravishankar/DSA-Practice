class Solution:
 def maximumCandies(self,candies:list[int],k:int)->int:
  if sum(candies)<k:return 0
  left,right,result=1,max(candies),0
  while left<=right:
   mid=(left+right)//2
   count=sum(c//mid for c in candies)
   if count>=k:result, left=mid,mid+1
   else:right=mid-1
  return result