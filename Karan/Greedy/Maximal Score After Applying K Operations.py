import heapq
import math
class Solution:
    def maxKelements(self, nums, k):
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        score = 0
        for _ in range(k):
            max_val = -heapq.heappop(max_heap)
            score += max_val
            heapq.heappush(max_heap, -math.ceil(max_val / 3))
        return score
nums = [1,10,3,3,3]
k = 3
sol = Solution()
print(sol.maxKelements(nums, k))