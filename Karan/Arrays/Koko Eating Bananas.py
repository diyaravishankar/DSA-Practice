import math
class Solution:
    def minEatingSpeed(self,p,h):
        l,r=1,max(p)
        while l<r:
            m=(l+r)//2
            if sum((x+m-1)//m for x in p)>h:l=m+1
            else:r=m
        return l