import bisect
class Solution:
  def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    heights = [h for _, h in envelopes]
    dp = []
    for h in heights:
      i = bisect.bisect_left(dp, h)
      if i == len(dp):
        dp.append(h)
      else:
        dp[i] = h
    return len(dp)