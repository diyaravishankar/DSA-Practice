class SegmentTree:
    def __init__(self,arr):
        self.n=len(arr)
        self.tree=[0]*(4*self.n)
        self.lazy=[0]*(4*self.n)
        self.build(1,0,self.n-1,arr)
    def build(self,node,l,r,arr):
        if l==r:
            self.tree[node]=arr[l]
            return
        m=(l+r)//2
        self.build(node*2,l,m,arr)
        self.build(node*2+1,m+1,r,arr)
        self.tree[node]=self.tree[node*2]+self.tree[node*2+1]
    def push(self,node,l,r):
        if self.lazy[node]:
            self.tree[node]=(r-l+1)-self.tree[node]
            if l!=r:
                self.lazy[node*2]^=1
                self.lazy[node*2+1]^=1
            self.lazy[node]=0
    def update(self,node,l,r,ql,qr):
        self.push(node,l,r)
        if ql>r or qr<l:
            return
        if ql<=l and r<=qr:
            self.lazy[node]^=1
            self.push(node,l,r)
            return
        m=(l+r)//2
        self.update(node*2,l,m,ql,qr)
        self.update(node*2+1,m+1,r,ql,qr)
        self.tree[node]=self.tree[node*2]+self.tree[node*2+1]
    def query(self,node,l,r,ql,qr):
        self.push(node,l,r)
        if ql>r or qr<l:
            return 0
        if ql<=l and r<=qr:
            return self.tree[node]
        m=(l+r)//2
        return self.query(node*2,l,m,ql,qr)+self.query(node*2+1,m+1,r,ql,qr)
    def total(self):
        return self.tree[1]
class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        st=SegmentTree(nums1)
        s=sum(nums2)
        ans=[]
        for q in queries:
            if q[0]==1:
                st.update(1,0,st.n-1,q[1],q[2])
            elif q[0]==2:
                s+=st.total()*q[1]
            else:
                ans.append(s)
        return ans