class TreeNode:
 def __init__(self, val=0, left=None, right=None):
  self.val = val
  self.left = left
  self.right = right
class Solution:
 def sumNumbers(self, root: TreeNode) -> int:
  def dfs(node, current):
   if not node:
    return 0
   current = current * 10 + node.val
   if not node.left and not node.right:
    return current
   return dfs(node.left, current) + dfs(node.right, current)
  return dfs(root, 0)