class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n, flip = len(s), []
        if s[0] == '0':
            flip.append(0)
        for i in range(1,n):
            if s[i] != s[i-1]:
                flip.append(i)
        if s[-1] == '0':
            flip.append(n)
        maxTree = SegTree([flip[j] - flip[j-1] + flip[j-2] - flip[j-3] for j in range(3, len(flip), 2)])
        res = []
        for l, r in queries:
            lPos, rPos = bisect_left(flip, l+1), bisect_left(flip, r+1)
            if rPos - lPos < 2 or rPos - lPos == 2 and lPos & 1 == 0:
                res.append(0)
            elif rPos - lPos == 2:
                res.append(r+1 - flip[rPos-1] + flip[lPos] - l)
            elif rPos - lPos == 3:
                if lPos & 1 == 0:
                    res.append(r+1 - flip[rPos-1] + flip[lPos+1] - flip[lPos])
                else:
                    res.append(flip[rPos-1] - flip[lPos+1] + flip[lPos] - l)
            else:
                change = 0
                if lPos & 1:
                    change = max(change, flip[lPos+2] - flip[lPos+1] + flip[lPos] - l)
                    lPos += 1
                if rPos & 1:
                    change = max(change, r+1 - flip[rPos-1] + flip[rPos-2] - flip[rPos-3])
                    rPos -= 1
                change = max(change, maxTree.query(lPos//2-1, rPos//2-1))
                res.append(change)
        ones = s.count('1')
        return [ones + change for change in res]
class SegTree:
    def __init__(self, arr: List[int]):
        self.n = 1 << (len(arr).bit_length())
        self.tree = [0] * (self.n << 1)
        for i, num in enumerate(arr, self.n):
            self.tree[i] = num
        for i in range(self.n-1, 0, -1):
            self.tree[i] = max(self.tree[i*2], self.tree[i*2+1])
    def query(self, l: int, r: int) -> int:
        l += self.n
        r += self.n
        res = 0
        while r-l > 1:
            if not l & 1:
                res = max(res, self.tree[l+1])
            if r & 1:
                res = max(res, self.tree[r-1])
            l >>= 1
            r >>= 1
        return res