from typing import List
class Solution:
 def fallingSquares(self, positions: List[List[int]]) -> List[int]:
  intervals = []
  res = []
  max_height = 0
  for left, size in positions:
   right = left + size
   height = size
   for l2, r2, h2 in intervals:
    if l2 < right and left < r2:
     height = max(height, h2 + size)
   intervals.append((left, right, height))
   max_height = max(max_height, height)
   res.append(max_height)
  return res