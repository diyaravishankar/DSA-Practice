class TreeNode:
 def __init__(self, val=0, left=None, right=None):
  self.val = val
  self.left = left
  self.right = right
class Solution:
 def maxPathSum(self, root: TreeNode) -> int:
  self.max_sum = float('-inf')
  def max_gain(node):
   if not node:
    return 0
   left_gain = max(max_gain(node.left), 0)
   right_gain = max(max_gain(node.right), 0)
   self.max_sum = max(self.max_sum, node.val + left_gain + right_gain)
   return node.val + max(left_gain, right_gain)
  max_gain(root)
  return self.max_sum