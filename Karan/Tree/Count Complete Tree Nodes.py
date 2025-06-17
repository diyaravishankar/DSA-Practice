class TreeNode:
 def __init__(self, val=0, left=None, right=None):
  self.val = val
  self.left = left
  self.right = right
class Solution:
 def countNodes(self, root: TreeNode) -> int:
  def height(node):
   h = 0
   while node:
    h += 1
    node = node.left
   return h
  if not root:
   return 0
  left = height(root.left)
  right = height(root.right)
  if left == right:
   return (1 << left) + self.countNodes(root.right)
  else:
   return (1 << right) + self.countNodes(root.left)