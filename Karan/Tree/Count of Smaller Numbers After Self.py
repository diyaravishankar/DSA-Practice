from typing import List
class Solution:
 def countSmaller(self, nums: List[int]) -> List[int]:
  n = len(nums)
  res = [0] * n
  indices = list(range(n))
  def merge_sort(start, end):
   if end - start <= 1:
    return
   mid = (start + end) // 2
   merge_sort(start, mid)
   merge_sort(mid, end)
   temp = []
   i, j = start, mid
   right_count = 0
   while i < mid and j < end:
    if nums[indices[j]] < nums[indices[i]]:
     temp.append(indices[j])
     right_count += 1
     j += 1
    else:
     res[indices[i]] += right_count
     temp.append(indices[i])
     i += 1
   while i < mid:
    res[indices[i]] += right_count
    temp.append(indices[i])
    i += 1
   while j < end:
    temp.append(indices[j])
    j += 1
   indices[start:end] = temp
  merge_sort(0, n)
  return res