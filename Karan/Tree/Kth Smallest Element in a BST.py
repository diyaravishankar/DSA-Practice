class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        return inorder(root)[k - 1]
sol = Solution()
root1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
print(sol.kthSmallest(root1, 1))
print(sol.kthSmallest(root2, 3))