class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        merged = {}
        for id_, val in nums1:
            merged[id_] = merged.get(id_, 0) + val
        for id_, val in nums2:
            merged[id_] = merged.get(id_, 0) + val
        return sorted([[id_, val] for id_, val in merged.items()])

sol = Solution()
print(sol.mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))
print(sol.mergeArrays([[2,4],[3,6],[5,5]], [[1,3],[4,3]]))