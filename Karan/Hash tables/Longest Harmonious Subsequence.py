from collections import Counter
class Solution:
 def findLHS(self, nums):
  count = Counter(nums)
  max_len = 0
  for key in count:
   if key + 1 in count:
    max_len = max(max_len, count[key] + count[key + 1])
  return max_len