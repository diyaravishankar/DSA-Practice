class Solution:
    def containsNearbyDuplicate(self,n,k):
        d={}
        for i,x in enumerate(n):
            if x in d and i-d[x]<=k:return True
            d[x]=i
        return False