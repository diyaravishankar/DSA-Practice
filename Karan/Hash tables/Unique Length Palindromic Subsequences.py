class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        for ch in set(s):
            first = s.find(ch)
            last = s.rfind(ch)
            if last - first > 1:
                mid_chars = set(s[first + 1:last])
                for c in mid_chars:
                    res.add((ch, c))
        return len(res)