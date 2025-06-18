class Node:
 def __init__(self, val=0, left=None, right=None, next=None):
  self.val = val
  self.left = left
  self.right = right
  self.next = next
class Solution:
 def connect(self, root: 'Node') -> 'Node':
  if not root or not root.left:
   return root
  root.left.next = root.right
  if root.next:
   root.right.next = root.next.left
  self.connect(root.left)
  self.connect(root.right)
  return root