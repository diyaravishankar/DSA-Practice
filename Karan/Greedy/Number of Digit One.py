class Solution:
 def countDigitOne(self, n: int) -> int:
  res = 0
  factor = 1
  while factor <= n:
   higher = n // (factor * 10)
   curr = (n // factor) % 10
   lower = n % factor
   if curr == 0:
    res += higher * factor
   elif curr == 1:
    res += higher * factor + lower + 1
   else:
    res += (higher + 1) * factor
   factor *= 10
  return res