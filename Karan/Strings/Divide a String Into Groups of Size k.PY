class Solution:
 def divideString(self, s: str, k: int, fill: str) -> list[str]:
  n = len(s)
  if n % k != 0:
   s += fill * (k - n % k)
  return [s[i:i + k] for i in range(0, len(s), k)]