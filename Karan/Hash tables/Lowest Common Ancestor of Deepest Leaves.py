class TreeNode:
 def __init__(s, v=0, l=None, r=None):
  s.val, s.left, s.right = v, l, r
class Solution:
 def lcaDeepestLeaves(s, r):
  def go(n):
   if not n: return 0, None
   ld, lcaL = go(n.left)
   rd, lcaR = go(n.right)
   return (ld + 1, lcaL) if ld > rd else (rd + 1, lcaR) if rd > ld else (ld + 1, n)
  return go(r)[1]