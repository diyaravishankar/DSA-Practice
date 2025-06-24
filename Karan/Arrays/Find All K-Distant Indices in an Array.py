class Solution:
 def findKDistantIndices(self, nums, key, k):
  key_indices = [i for i, num in enumerate(nums) if num == key]
  result = set()
  