class Solution:
 def mostPoints(self, questions: list[list[int]]) -> int:
  n=len(questions)
  dp=[0]*n
  dp[-1]=questions[-1][0]
  for i in range(n-2,-1,-1):
   points,brainpower=questions[i]
   next_q=i+brainpower+1
   dp[i]=max(points+(dp[next_q] if next_q<n else 0),dp[i+1])
  return dp[0]