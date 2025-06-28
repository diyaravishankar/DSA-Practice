from bisect import bisect_left, bisect_right
class RangeModule:
 def __init__(self):
  self.intervals = []
 def addRange(self, left: int, right: int) -> None:
  new_intervals = []
  placed = False
  for l, r in self.intervals:
   if r < left:
    new_intervals.append((l, r))
   elif right < l:
    if not placed:
     new_intervals.append((left, right))
     placed = True
    new_intervals.append((l, r))
   else:
    left = min(left, l)
    right = max(right, r)
  if not placed:
   new_intervals.append((left, right))
  self.intervals = new_intervals
 def queryRange(self, left: int, right: int) -> bool:
  for l, r in self.intervals:
   if l <= left and right <= r:
    return True
   if r > left:
    break
  return False
 def removeRange(self, left: int, right: int) -> None:
  new_intervals = []
  for l, r in self.intervals:
   if r <= left or right <= l:
    new_intervals.append((l, r))
   else:
    if l < left:
     new_intervals.append((l, left))
    if right < r:
     new_intervals.append((right, r))
  self.intervals = new_intervals