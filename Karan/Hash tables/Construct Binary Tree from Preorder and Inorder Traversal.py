class Solution:
 def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
  idx_map = {val: i for i, val in enumerate(inorder)}
  self.pre_idx = 0
  def helper(left: int, right: int) -> Optional[TreeNode]:
   if left > right:
    return None
   root_val = preorder[self.pre_idx]
   self.pre_idx += 1
   root = TreeNode(root_val)
   index = idx_map[root_val]
   root.left = helper(left, index - 1)
   root.right = helper(index + 1, right)
   return root
  return helper(0, len(inorder) - 1)