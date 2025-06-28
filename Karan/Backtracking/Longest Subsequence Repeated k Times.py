from collections import Counter, deque
class Solution:
 def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
  ans = ""
  candidate = sorted([c for c, w in Counter(s).items() if w >= k], reverse=True)
  q = deque(candidate)
  while q:
   curr = q.popleft()
   if len(curr) > len(ans) or (len(curr) == len(ans) and curr > ans):
    ans = curr
   for ch in candidate:
    nxt = curr + ch
    it = iter(s)
    if all(c in it for c in nxt * k):
     q.append(nxt)
  return ans