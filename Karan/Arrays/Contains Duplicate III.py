class Solution:
    def containsNearbyAlmostDuplicate(self,n,k,t):
        if t<0:return False
        b={}
        w=t+1
        for i,x in enumerate(n):
            m=x//w
            if m in b or m-1 in b and x-b[m-1]<w or m+1 in b and b[m+1]-x<w:return True
            b[m]=x
            if i>=k:del b[n[i-k]//w]
        return False