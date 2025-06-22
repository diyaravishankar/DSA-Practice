from collections import defaultdict
from math import gcd
class Solution:
 def maxPoints(self, points: list[list[int]]) -> int:
  n = len(points)
  if n <= 2:
   return n
  res = 0
  for i in range(n):
   slope_count = defaultdict(int)
   same = 1
   for j in range(i + 1, n):
    x1, y1 = points[i]
    x2, y2 = points[j]
    dx, dy = x2 - x1, y2 - y1
    if dx == 0 and dy == 0:
     same += 1
    else:
     g = gcd(dx, dy)
     dx //= g
     dy //= g
     if dx < 0:
      dx, dy = -dx, -dy
     elif dx == 0:
      dy = abs(dy)
     slope_count[(dx, dy)] += 1
   res = max(res, same + max(slope_count.values(), default=0))
  return res