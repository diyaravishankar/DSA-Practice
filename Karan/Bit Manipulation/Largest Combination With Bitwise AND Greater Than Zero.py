class Solution:
 def largestCombination(s, A):
  return max(sum((x >> i) & 1 for x in A) for i in range(24))