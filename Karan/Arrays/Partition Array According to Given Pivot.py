class Solution:
    def pivotArray(self, nums, pivot):
        left, middle, right = [], [], []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                middle.append(num)
        return left + middle + right
sol = Solution()
print(sol.pivotArray([9, 12, 5, 10, 14, 3, 10], 10))
print(sol.pivotArray([-3, 4, 3, 2], 2))