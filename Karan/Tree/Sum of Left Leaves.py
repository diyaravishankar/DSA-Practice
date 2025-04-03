class Solution:
 def sumOfLeftLeaves(self, root):
  if not root: return 0
  left_sum = 0
  if root.left and not root.left.left and not root.left.right:
   left_sum = root.left.val
  return left_sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)