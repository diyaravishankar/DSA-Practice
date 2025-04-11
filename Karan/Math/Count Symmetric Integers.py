class Solution:
 def countSymmetricIntegers(self, low: int, high: int) -> int:
  def is_symmetric(x: int) -> bool:
   s = str(x)
   if len(s) % 2 != 0:
    return False
   n = len(s) // 2
   return sum(map(int, s[:n])) == sum(map(int, s[n:]))
  return sum(1 for x in range(low, high + 1) if is_symmetric(x))