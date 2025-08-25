class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
class Solution:
    def preorder(self, root):
        if not root:
            return []
        res=[root.val]
        for child in root.children:
            res.extend(self.preorder(child))
        return res