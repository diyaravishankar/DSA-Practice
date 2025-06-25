class Solution:
 def closestToTarget(self, arr: List[int], target: int) -> int:
  s = set()
  res = float('inf')
  for num in arr:
   new_s = {num}
   for val in s:
    new_s.add(val & num)
   s = new_s
   for val in s:
    res = min(res, abs(val - target))
  return res