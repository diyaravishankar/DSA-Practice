from heapq import heappush, heappop
import sys
class Solution:
    def smallestRange(self, nums):
        min_heap = []
        max_val = -sys.maxsize
        range_start, range_end = 0, sys.maxsize
        for i in range(len(nums)):
            heappush(min_heap, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])
        while min_heap:
            min_val, row, idx = heappop(min_heap)
            if max_val - min_val < range_end - range_start:
                range_start, range_end = min_val, max_val
            if idx + 1 < len(nums[row]):
                next_val = nums[row][idx + 1]
                heappush(min_heap, (next_val, row, idx + 1))
                max_val = max(max_val, next_val)
            else:
                break
        return [range_start, range_end]
nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
sol = Solution()
print(sol.smallestRange(nums)) 