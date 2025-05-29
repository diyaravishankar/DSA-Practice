class Solution:
 def mincostTickets(self, days, costs):
  day_set=set(days)
  max_day=days[-1]
  dp=[0]*(max_day+1)
  for i in range(1,max_day+1):
   if i not in day_set:
    dp[i]=dp[i-1]
   else:
    dp[i]=min(
     dp[i-1]+costs[0],
     dp[max(0,i-7)]+costs[1],
     dp[max(0,i-30)]+costs[2]
    )
  return dp[max_day]