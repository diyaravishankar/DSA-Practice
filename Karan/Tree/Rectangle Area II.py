from typing import List
class Solution:
 def rectangleArea(self, rectangles: List[List[int]]) -> int:
  MOD = 10**9 + 7
  events = []
  for x1, y1, x2, y2 in rectangles:
   events.append((y1, 1, x1, x2)) 
   events.append((y2, -1, x1, x2))
  events.sort()
  def merge(intervals):
   merged = []
   for start, end in sorted(intervals):
    if not merged or merged[-1][1] < start:
     merged.append([start, end])
    else:
     merged[-1][1] = max(merged[-1][1], end)
   return merged
  active = []
  prev_y = 0
  area = 0
  for y, typ, x1, x2 in events:
   merged = merge(active)
   total_x = sum(end - start for start, end in merged)
   area += total_x * (y - prev_y)
   if typ == 1:
    active.append([x1, x2])
   else:
    active.remove([x1, x2])
   prev_y = y
  return area % MOD