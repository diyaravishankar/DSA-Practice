class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = {'a': 0, 'b': 0, 'c': 0}
        l, r, res = 0, 0, 0
        for r in range(len(s)):
            cnt[s[r]] += 1
            while all(cnt[ch] > 0 for ch in 'abc'):
                res += len(s) - r
                cnt[s[l]] -= 1
                l += 1
        return res