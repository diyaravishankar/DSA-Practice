class Solution:
 def minCut(self, s: str) -> int:
  n = len(s)
  is_palindrome = [[False] * n for _ in range(n)]
  for end in range(n):
   for start in range(end + 1):
    if s[start] == s[end] and (end - start <= 2 or is_palindrome[start + 1][end - 1]):
     is_palindrome[start][end] = True
  dp = [0] * n
  for i in range(n):
   if is_palindrome[0][i]:
    dp[i] = 0
   else:
    dp[i] = i
    for j in range(1, i + 1):
     if is_palindrome[j][i]:
      dp[i] = min(dp[i], dp[j - 1] + 1)
  return dp[-1]