class Solution:
 def maxUniqueSplit(self,s:str)->int:
  def backtrack(i,seen):
   if i==len(s):return len(seen)
   max_splits=0
   for j in range(i+1,len(s)+1):
    sub=s[i:j]
    if sub not in seen:
     seen.add(sub)
     max_splits=max(max_splits,backtrack(j,seen))
     seen.remove(sub)
   return max_splits
  return backtrack(0,set())