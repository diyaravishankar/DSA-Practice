class Solution:
    def removeDuplicates(self,n):
        i=0
        for x in n:
            if i<1 or n[i-1]!=x:
                n[i]=x
                i+=1
        return 