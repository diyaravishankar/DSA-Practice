class Solution:
    def duplicateZeros(self,a):
        n=len(a)
        i=0
        while i<n:
            if a[i]==0:
                a[i+1:n]=a[i:n-1]
                i+=1
            i+=1