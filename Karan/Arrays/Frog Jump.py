class Solution:
 def canCross(self, stones):
  stone_set = set(stones)
  cache = {}
  def jump_frog(pos, jump):
   if pos == stones[-1]: return True
   if (pos, jump) in cache: return cache[(pos, jump)]
   for step in (jump - 1, jump, jump + 1):
    if step > 0 and pos + step in stone_set:
     if jump_frog(pos + step, step):
      cache[(pos, jump)] = True
      return True
   cache[(pos, jump)] = False
   return False
  return jump_frog(0, 0)