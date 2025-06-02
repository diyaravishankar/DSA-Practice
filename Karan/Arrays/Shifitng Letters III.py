class Solution:
 def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
  n = len(s)
  diff = [0] * (n + 1)
  for start, end, direction in shifts:
   diff[start] += 1 if direction == 1 else -1
   diff[end + 1] -= 1 if direction == 1 else -1
  for i in range(1, n):
   diff[i] += diff[i - 1]
  res = []
  for i in range(n):
   shift = (ord(s[i]) - ord('a') + diff[i]) % 26
   res.append(chr(shift + ord('a')))
  return ''.join(res)