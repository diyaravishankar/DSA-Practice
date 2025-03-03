class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
sol = Solution()
root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
p = root.left
q = root.right
print(sol.lowestCommonAncestor(root, p, q).val)
p = root.left
q = root.left.right
print(sol.lowestCommonAncestor(root, p, q).val)
root2 = TreeNode(2, TreeNode(1))
p = root2
q = root2.left
print(sol.lowestCommonAncestor(root2, p, q).val)