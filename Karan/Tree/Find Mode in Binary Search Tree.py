class Solution:
 def findMode(self, root):
  self.prev = None
  self.count = 0
  self.maxCount = 0
  self.modes = []
  def inorder(node):
   if not node:
    return
   inorder(node.left)
   if self.prev == node.val:
    self.count += 1
   else:
    self.count = 1
   if self.count > self.maxCount:
    self.maxCount = self.count
    self.modes = [node.val]
   elif self.count == self.maxCount:
    self.modes.append(node.val)
   self.prev = node.val
   inorder(node.right)
  inorder(root)
  return self.modes