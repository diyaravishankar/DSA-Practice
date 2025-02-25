class Solution:
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        return "".join("1" if nums[i][i] == "0" else "0" for i in range(n))
solution = Solution()
print(solution.findDifferentBinaryString(["01", "10"]))
print(solution.findDifferentBinaryString(["00", "01"]))
print(solution.findDifferentBinaryString(["111", "011", "001"]))