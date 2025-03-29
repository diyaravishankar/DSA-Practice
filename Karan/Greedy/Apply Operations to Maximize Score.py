import sys, heapq, math
class Solution:
 MOD = 10**9 + 7
 def maximumScore(self, nums, k):
  n = len(nums)
  prime_scores = [0] * n
  for i in range(n):
   num = nums[i]
   for f in range(2, int(math.sqrt(num)) + 1):
    if num % f == 0:
     prime_scores[i] += 1
     while num % f == 0:
      num //= f
   if num >= 2:
    prime_scores[i] += 1
  next_dominant = [n] * n
  prev_dominant = [-1] * n
  stack = []
  for i in range(n):
   while stack and prime_scores[stack[-1]] < prime_scores[i]:
    next_dominant[stack.pop()] = i
   if stack:
    prev_dominant[i] = stack[-1]
   stack.append(i)
  num_of_subarrays = [(next_dominant[i] - i) * (i - prev_dominant[i]) for i in range(n)]
  pq = [(-nums[i], i) for i in range(n)]
  heapq.heapify(pq)
  score = 1
  def _power(base, exp):
   res = 1
   while exp:
    if exp % 2:
     res = (res * base) % self.MOD
    base = (base * base) % self.MOD
    exp //= 2
   return res
  while k > 0:
   num, i = heapq.heappop(pq)
   num = -num
   ops = min(k, num_of_subarrays[i])
   score = (score * _power(num, ops)) % self.MOD
   k -= ops
  return score