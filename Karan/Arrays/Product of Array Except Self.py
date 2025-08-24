class Solution:
    def productExceptSelf(self,n):
        m=len(n)
        l=[1]*m
        r=[1]*m
        for i in range(1,m):l[i]=l[i-1]*n[i-1]
        for i in range(m-2,-1,-1):r[i]=r[i+1]*n[i+1]
        return [l[i]*r[i] for i in range(m)]