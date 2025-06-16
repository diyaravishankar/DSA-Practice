class Solution:
 def buildTree(self, inorder, postorder):
  inorder_index = {val: idx for idx, val in enumerate(inorder)}
  self.post_idx = len(postorder) - 1
  def helper(left, right):
   if left > right:
    return None
   root_val = postorder[self.post_idx]
   self.post_idx -= 1
   root = TreeNode(root_val)
   idx = inorder_index[root_val]
   root.right = helper(idx + 1, right)
   root.left = helper(left, idx - 1)
   return root
  return helper(0, len(inorder) - 1)