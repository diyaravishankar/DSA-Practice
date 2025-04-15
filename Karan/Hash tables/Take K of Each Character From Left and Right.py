class Solution:
 def takeCharacters(self, s, k):
  from collections import Counter
  n=len(s)
  count=Counter(s)
  if any(count[ch]<k for ch in 'abc'):return -1
  need={'a':count['a']-k,'b':count['b']-k,'c':count['c']-k}
  maxlen=0
  left=0
  curr={'a':0,'b':0,'c':0}
  for right in range(n):
   curr[s[right]]+=1
   while any(curr[ch]>need[ch] for ch in 'abc'):
    curr[s[left]]-=1
    left+=1
   maxlen=max(maxlen,right-left+1)
  return n-maxlen