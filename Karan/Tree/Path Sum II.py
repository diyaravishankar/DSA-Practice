class Solution:
 def pathSum(self,root,targetSum):
  res=[]
  def dfs(node,path,total):
   if not node:return
   path.append(node.val)
   total+=node.val
   if not node.left and not node.right and total==targetSum:
    res.append(path[:])
   dfs(node.left,path,total)
   dfs(node.right,path,total)
   path.pop()
  dfs(root,[],0)
  return res