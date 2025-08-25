class Solution:
    def maximumUniqueSubarray(self, nums):
        seen = set()
        left = 0
        total = 0
        res = 0
        for right, val in enumerate(nums):
            while val in seen:
                seen.remove(nums[left])
                total -= nums[left]
                left += 1
            seen.add(val)
            total += val
            res = max(res, total)
        return res