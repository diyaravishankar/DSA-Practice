class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        strs.sort()
        first, last = strs[0], strs[-1]
        prefix = ""
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                prefix += first[i]
            else:
                break
        return prefix
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"])) 
print(solution.longestCommonPrefix(["dog","racecar","car"]))   