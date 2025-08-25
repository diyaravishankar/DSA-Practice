class Solution:
    def containsDuplicate(self,n):
        s=set()
        for x in n:
            if x in s:return True
            s.add(x)
        return False