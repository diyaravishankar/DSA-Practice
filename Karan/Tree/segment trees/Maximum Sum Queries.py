import bisect
class SegTree:
    def __init__(self,vals):
        self.n=len(vals)
        self.tree=[-1]*(self.n*4)
    def update(self,node,l,r,pos,val):
        if l==r:
            self.tree[node]=max(self.tree[node],val)
            return
        m=(l+r)//2
        if pos<=m:
            self.update(node*2,l,m,pos,val)
        else:
            self.update(node*2+1,m+1,r,pos,val)
        self.tree[node]=max(self.tree[node*2],self.tree[node*2+1])
    def query(self,node,l,r,ql,qr):
        if ql>r or qr<l:
            return -1
        if ql<=l and r<=qr:
            return self.tree[node]
        m=(l+r)//2
        return max(self.query(node*2,l,m,ql,qr),self.query(node*2+1,m+1,r,ql,qr))
class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n=len(nums1)
        points=[(nums1[i],nums2[i],nums1[i]+nums2[i]) for i in range(n)]
        vals=sorted(set(nums2))
        comp={v:i for i,v in enumerate(vals)}
        tree=SegTree(vals)
        points.sort(reverse=True)
        qs=[(x,y,i) for i,(x,y) in enumerate(queries)]
        qs.sort(reverse=True)
        ans=[-1]*len(queries)
        j=0
        for x,y,i in qs:
            while j<n and points[j][0]>=x:
                idx=comp[points[j][1]]
                tree.update(1,0,tree.n-1,idx,points[j][2])
                j+=1
            idx=bisect.bisect_left(vals,y)
            if idx<tree.n:
                ans[i]=tree.query(1,0,tree.n-1,idx,tree.n-1)
        return ans