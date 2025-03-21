class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = -1
        for num in sorted(num_set):
            length, current = 1, num
            while current * current in num_set:
                current *= current
                length += 1
            if length > 1:
                max_length = max(max_length, length)
        return max_length