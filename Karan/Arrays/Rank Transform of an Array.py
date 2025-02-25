class Solution:
 def arrayRankTransform(self,arr):
  sorted_arr=sorted(set(arr))
  rank={num:i+1 for i,num in enumerate(sorted_arr)}
  return [rank[num] for num in arr]