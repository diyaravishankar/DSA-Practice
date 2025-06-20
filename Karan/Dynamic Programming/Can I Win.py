class Solution:
 def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
  if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
   return False
  if desiredTotal <= 0:
   return True
  memo = {}
  def can_win(used, total):
   if used in memo:
    return memo[used]
   for i in range(1, maxChoosableInteger + 1):
    mask = 1 << i
    if used & mask == 0:
     if i >= total or not can_win(used | mask, total - i):
      memo[used] = True
      return True
   memo[used] = False
   return False
  return can_win(0, desiredTotal)