class TreeNode:
 def __init__(self, val=0, left=None, right=None):
  self.val = val
  self.left = left
  self.right = right
class Solution:
 def preorderTraversal(self, root: TreeNode) -> list[int]:
  result = []
  def dfs(node):
   if not node:
    return
   result.append(node.val)
   dfs(node.left)
   dfs(node.right)
  dfs(root)
  return result