class Solution:
 def generateTrees(self, n):
  if n == 0:
   return []
  def build(start, end):
   if start > end:
    return [None]
   all_trees = []
   for i in range(start, end + 1):
    left_trees = build(start, i - 1)
    right_trees = build(i + 1, end)
    for l in left_trees:
     for r in right_trees:
      root = TreeNode(i)
      root.left = l
      root.right = r
      all_trees.append(root)
   return all_trees
  return build(1, n)