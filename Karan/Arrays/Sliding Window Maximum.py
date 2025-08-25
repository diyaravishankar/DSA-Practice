from collections import deque
class Solution:
    def maxSlidingWindow(self,n,k):
        d=deque()
        r=[]
        for i,x in enumerate(n):
            while d and n[d[-1]]<x:d.pop()
            d.append(i)
            if d[0]<=i-k:d.popleft()
            if i>=k-1:r.append(n[d[0]])
        return r