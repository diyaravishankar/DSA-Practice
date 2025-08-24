class Solution:
    def minimumSum(self,g):
        m,n=len(g),len(g[0])
        o=[(i,j) for i in range(m) for j in range(n) if g[i][j]]
        def ar(s):
            r1=min(i for i,_ in s);r2=max(i for i,_ in s)
            c1=min(j for _,j in s);c2=max(j for _,j in s)
            return (r2-r1+1)*(c2-c1+1)
        a=float('inf')
        for c1 in range(n-2):
            for c2 in range(c1+1,n-1):
                p1=[x for x in o if x[1]<=c1]
                p2=[x for x in o if c1<x[1]<=c2]
                p3=[x for x in o if x[1]>c2]
                if p1 and p2 and p3:a=min(a,ar(p1)+ar(p2)+ar(p3))
        for r1 in range(m-2):
            for r2 in range(r1+1,m-1):
                p1=[x for x in o if x[0]<=r1]
                p2=[x for x in o if r1<x[0]<=r2]
                p3=[x for x in o if x[0]>r2]
                if p1 and p2 and p3:a=min(a,ar(p1)+ar(p2)+ar(p3))
        for r in range(m-1):
            for c in range(n-1):
                A=[x for x in o if x[0]<=r and x[1]<=c]
                B=[x for x in o if x[0]<=r and x[1]>c]
                C=[x for x in o if x[0]>r and x[1]<=c]
                D=[x for x in o if x[0]>r and x[1]>c]
                if A and B and C and D:a=min(a,ar(A)+ar(B)+ar(C+D),ar(C)+ar(D)+ar(A+B))
                if (A or C) and B and D:a=min(a,ar(A+C)+ar(B)+ar(D))
                if (B or D) and A and C:a=min(a,ar(B+D)+ar(A)+ar(C))
        return a