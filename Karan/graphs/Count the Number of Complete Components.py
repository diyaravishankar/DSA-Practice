from collections import defaultdict
class Solution:
 def countCompleteComponents(self, n, edges):
  graph = defaultdict(set)
  for u, v in edges:
   graph[u].add(v)
   graph[v].add(u)
  visited = set()
  complete_components = 0
  def dfs(node, component):
   visited.add(node)
   component.add(node)
   for neighbor in graph[node]:
    if neighbor not in visited:
     dfs(neighbor, component)
  for node in range(n):
   if node not in visited:
    component = set()
    dfs(node, component)
    size = len(component)
    if all(len(graph[v]) == size - 1 for v in component):
     complete_components += 1
  return complete_components