class Solution:
 def hasPathSum(self, root, targetSum):
  if not root:
   return False
  if not root.left and not root.right:
   return root.val == targetSum
  return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)