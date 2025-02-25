class Solution:
    def minExtraChar(self, s: str, dictionary: list) -> int:
        n = len(s)
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for word in dictionary:
                if i >= len(word) and s[i - len(word):i] == word:
                    dp[i] = min(dp[i], dp[i - len(word)])
        return dp[n]
solution = Solution()
print(solution.minExtraChar("leetscode", ["leet", "code", "leetcode"]))
print(solution.minExtraChar("sayhelloworld", ["hello", "world"]))