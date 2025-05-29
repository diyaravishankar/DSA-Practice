class Solution:
 def countPalindromicSubsequence(self, s):
  res=set()
  for c in set(s):
   l=s.find(c)
   r=s.rfind(c)
   if l<r:
    mid=set(s[l+1:r])
    for m in mid:
     res.add(c+m+c)
  return len(res)