from collections import deque, defaultdict
class Solution:
 def count_parity(self, tree, size):
  adj=defaultdict(list)
  for u,v in tree:
   adj[u].append(v)
   adj[v].append(u)
  parity=[0]*size
  visited=[False]*size
  queue=deque([(0,0)])
  even=odd=0
  while queue:
   node,level=queue.popleft()
   if visited[node]:
    continue
   visited[node]=True
   parity[node]=level%2
   if level%2==0:
    even+=1
   else:
    odd+=1
   for nei in adj[node]:
    if not visited[nei]:
     queue.append((nei,level+1))
  return parity,even,odd
 def maxTargetNodes(self, edges1, edges2):
  n=len(edges1)+1
  m=len(edges2)+1
  parity1,even1,odd1=self.count_parity(edges1,n)
  _,even2,odd2=self.count_parity(edges2,m)
  res=[]
  for i in range(n):
   p1=parity1[i]
   in_tree1=even1 if p1==0 else odd1
   opt1=in_tree1+(even2 if p1%2==0 else odd2)
   opt2=in_tree1+(odd2 if p1%2==0 else even2)
   res.append(max(opt1,opt2))
  return res