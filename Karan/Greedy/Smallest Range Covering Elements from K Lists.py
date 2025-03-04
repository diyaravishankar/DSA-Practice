from heapq import heappush, heappop
class Solution:
 def smallestRange(self, nums):
  min_heap = []
  max_value = float('-inf')
  for i in range(len(nums)):
   heappush(min_heap, (nums[i][0], i, 0))
   max_value = max(max_value, nums[i][0])
  start, end = float('-inf'), float('inf')
  while min_heap:
   min_value, row, col = heappop(min_heap)
   if max_value - min_value < end - start:
    start, end = min_value, max_value
   if col + 1 == len(nums[row]):
    return [start, end]
   next_value = nums[row][col + 1]
   heappush(min_heap, (next_value, row, col + 1))
   max_value = max(max_value, next_value)