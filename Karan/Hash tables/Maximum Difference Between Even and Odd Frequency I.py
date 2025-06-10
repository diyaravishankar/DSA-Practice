class Solution:
 def maxDifference(self, s: str) -> int:
  freq = [0] * 26
  for ch in s:
   freq[ord(ch) - ord('a')] += 1
  max_diff = float('-inf')
  for i in range(26):
   if freq[i] % 2 == 1:
    for j in range(26):
     if freq[j] % 2 == 0 and freq[j] > 0:
      max_diff = max(max_diff, freq[i] - freq[j])
  return max_diff