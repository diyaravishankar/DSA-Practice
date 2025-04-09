class Solution:
 def resultsArray(self, nums, k):
  n = len(nums)
  res = []
  for i in range(n - k + 1):
   window = nums[i:i + k]
   if all(window[j] + 1 == window[j + 1] for j in range(k - 1)):
    res.append(window[-1])
   else:
    res.append(-1)
  return res