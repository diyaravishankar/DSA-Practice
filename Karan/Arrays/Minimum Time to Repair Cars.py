class Solution:
 def repairCars(self, ranks, cars):
  def canFix(t):
   cnt = 0
   for r in ranks:
    cnt += int((t // r) ** 0.5)
    if cnt >= cars: return True
   return False
  l, r = 1, min(ranks) * cars * cars
  while l < r:
   m = (l + r) // 2
   if canFix(m): r = m
   else: l = m + 1
  return l
s = Solution()
print(s.repairCars([4,2,3,1], 10))
print(s.repairCars([5,1,8], 6))