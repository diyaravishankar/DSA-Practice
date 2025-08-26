class SegTree:
    def __init__(self,n):
        self.size=1
        while self.size<=n:
            self.size<<=1
        self.tree=[0]*(2*self.size)
    def update(self,pos,val):
        pos+=self.size
        if self.tree[pos]>=val:
            return
        self.tree[pos]=val
        pos//=2
        while pos:
            left=self.tree[2*pos]
            right=self.tree[2*pos+1]
            self.tree[pos]=left if left>right else right
            pos//=2
    def query(self,l,r):
        if l>r:
            return 0
        l+=self.size
        r+=self.size
        res=0
        while l<=r:
            if l&1:
                if self.tree[l]>res:
                    res=self.tree[l]
                l+=1
            if not r&1:
                if self.tree[r]>res:
                    res=self.tree[r]
                r-=1
            l//=2
            r//=2
        return res
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        MAX=max(nums)
        seg=SegTree(MAX)
        ans=0
        for num in nums:
            left=num-k
            if left<1:
                left=1
            right=num-1
            best_prev=seg.query(left,right) if left<=right else 0
            dp=best_prev+1
            seg.update(num,dp)
            if dp>ans:
                ans=dp
        return ans