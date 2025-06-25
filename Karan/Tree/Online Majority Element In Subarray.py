import random
import bisect
from collections import defaultdict
class MajorityChecker:
 def __init__(self, arr):
  self.arr = arr
  self.pos = defaultdict(list)
  for i, num in enumerate(arr):
   self.pos[num].append(i)
 def query(self, left, right, threshold):
  for _ in range(20):
   candidate = self.arr[random.randint(left, right)]
   count = self.count_occurrences(candidate, left, right)
   if count >= threshold:
    return candidate
  return -1
 def count_occurrences(self, num, left, right):
  idxs = self.pos[num]
  l = bisect.bisect_left(idxs, left)
  r = bisect.bisect_right(idxs, right)
  return r - l