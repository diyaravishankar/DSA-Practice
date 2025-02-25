from collections import Counter
class Solution:
 def canArrange(self,arr,k):
  freq=Counter(x%k for x in arr)
  if freq[0]%2!=0:
   return False
  for i in range(1,k//2+1):
   if freq[i]!=freq[k-i]:
    return False
  return True