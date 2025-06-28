from collections import defaultdict
from bisect import bisect_left, bisect_right
class RangeFreqQuery:
 def __init__(self, arr: List[int]):
  self.pos = defaultdict(list)
  for i, val in enumerate(arr):
   self.pos[val].append(i)
 def query(self, left: int, right: int, value: int) -> int:
  idxs = self.pos[value]
  return bisect_right(idxs, right) - bisect_left(idxs, left)