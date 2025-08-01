class Solution:
 def numTrees(self, n: int) -> int:
  dp = [0] * (n + 1)
  dp[0] = 1
  for nodes in range(1, n + 1):
   for root in range(1, nodes + 1):
    dp[nodes] += dp[root - 1] * dp[nodes - root]
  return dp[n]