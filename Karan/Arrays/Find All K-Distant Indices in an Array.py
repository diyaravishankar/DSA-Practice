class Solution:
 def findKDistantIndices(self, nums, key, k):
  key_indices = [i for i, num in enumerate(nums) if num == key]
  result = set()
  for idx in key_indices:
   for i in range(max(0, idx - k), min(len(nums), idx + k + 1)):
    