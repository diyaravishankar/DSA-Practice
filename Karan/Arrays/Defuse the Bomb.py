class Solution:
 def decrypt(self, code, k):
  n = len(code)
  if k == 0:
   return [0] * n
  res = [0] * n
  for i in range(n):
   total = 0
   for j in range(1, abs(k) + 1):
    if k > 0:
     total += code[(i + j) % n]
    else:
     total += code[(i - j + n) % n]
   res[i] = total
  return res