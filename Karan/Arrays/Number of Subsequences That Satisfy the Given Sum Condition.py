class Solution:
 def numSubseq(self, nums, target):
  nums.sort()
  mod = 10**9 + 7
  n = len(nums)
  power = [1] * n
  for i in range(1, n):
   power[i] = (power[i - 1] * 2) % mod
  left, right = 0, n - 1
  res = 0
  while left <= right:
   if nums[left] + nums[right] <= target:
    res = (res + power[right - left]) % mod
    left += 1
   else:
    right -= 1
  return res