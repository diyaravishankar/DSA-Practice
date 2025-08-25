class Solution:
    def search(self,n,t):
        l,r=0,len(n)-1
        while l<=r:
            m=(l+r)//2
            if n[m]==t:return m
            if n[m]<t:l=m+1
            else:r=m-1
        return -1