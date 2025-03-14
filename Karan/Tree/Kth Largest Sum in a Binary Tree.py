from collections import deque
import heapq
class Solution:
 def kthLargestLevelSum(self, root:Optional[TreeNode], k:int)->int:
  q=deque([root])
  minHeap=[]
  while q:
   levelSum=sum(node.val for node in q)
   heapq.heappush(minHeap,levelSum)
   if len(minHeap)>k:heapq.heappop(minHeap)
   for _ in range(len(q)):
    node=q.popleft()
    if node.left:q.append(node.left)
    if node.right:q.append(node.right)
  return minHeap[0] if len(minHeap)==k else -1