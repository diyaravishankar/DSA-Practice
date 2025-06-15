class DSU:
 def __init__(self, n):
  self.parent = list(range(n))
 def find(self, x):
  if self.parent[x] != x:
   self.parent[x] = self.find(self.parent[x])
  return self.parent[x]
 def union(self, x, y):
  self.parent[self.find(x)] = self.find(y)
class Solution:
 def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
  n = len(nums)
  dsu = DSU(n)
  val_index = sorted([(val, i) for i, val in enumerate(nums)])
  for i in range(n - 1):
   if abs(val_index[i][0] - val_index[i + 1][0]) <= limit:
    dsu.union(val_index[i][1], val_index[i + 1][1])
  groups = {}
  for i in range(n):
   root = dsu.find(i)
   if root not in groups:
    groups[root] = []
   groups[root].append(i)
  res = nums[:]
  for idxs in groups.values():
   sorted_idxs = sorted(idxs)
   sorted_vals = sorted(nums[i] for i in sorted_idxs)
   for i, val in zip(sorted_idxs, sorted_vals):
    res[i] = val
  return res