from heapq import heappop, heappush
class Solution:
 def countPaths(self, n, roads):
  mod=10**9+7
  graph={i:[] for i in range(n)}
  for u,v,time in roads:
   graph[u].append((v,time))
   graph[v].append((u,time))
  dist=[float('inf')]*n
  ways=[0]*n
  dist[0]=0
  ways[0]=1
  pq=[(0,0)]
  while pq:
   d,u=heappop(pq)
   if d>dist[u]:continue
   for v,time in graph[u]:
    new_dist=d+time
    if new_dist<dist[v]:
     dist[v]=new_dist
     ways[v]=ways[u]
     heappush(pq,(new_dist,v))
    elif new_dist==dist[v]:
     ways[v]=(ways[v]+ways[u])%mod
  return ways[n-1]