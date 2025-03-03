class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root, low=float('-inf'), high=float('inf')):
        if not root:
            return True
        if root.val <= low or root.val >= high:
            return False
        return self.isValidBST(root.left, low, root.val) and self.isValidBST(root.right, root.val, high)
sol = Solution()
root1 = TreeNode(2, TreeNode(1), TreeNode(3))
root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(sol.isValidBST(root1))
print(sol.isValidBST(root2))