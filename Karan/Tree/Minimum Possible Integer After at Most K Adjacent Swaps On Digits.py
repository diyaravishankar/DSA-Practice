import bisect
class BIT:
 def __init__(self, n):
  self.bit = [0] * (n + 2)
 def update(self, i, delta):
  i += 1
  while i < len(self.bit):
   self.bit[i] += delta
   i += i & -i
 def query(self, i):
  i += 1
  res = 0
  while i > 0:
   res += self.bit[i]
   i -= i & -i
  return res
class Solution:
 def minInteger(self, num: str, k: int) -> str:
  from collections import deque
  pos = [deque() for _ in range(10)]
  for i, ch in enumerate(num):
   pos[int(ch)].append(i)
  n = len(num)
  bit = BIT(n)
  res = []
  for _ in range(n):
   for d in range(10):
    if pos[d]:
     idx = pos[d][0]
     cost = idx - bit.query(idx - 1)
     if cost <= k:
      k -= cost
      bit.update(idx, 1)
      res.append(str(d))
      pos[d].popleft()
      break
  return ''.join(res)