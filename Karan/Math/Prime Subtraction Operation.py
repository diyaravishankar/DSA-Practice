class Solution:
 def prime_list(self, n):
  primes = []
  is_prime = [True] * (n + 1)
  for p in range(2, n + 1):
   if is_prime[p]:
    primes.append(p)
    for multiple in range(p * p, n + 1, p):
     is_prime[multiple] = False
  return primes
 def primeSubOperation(self, nums):
  primes = self.prime_list(1000)
  for i in range(len(nums)):
   for p in reversed(primes):
    if p < nums[i] and (i == 0 or nums[i] - p > nums[i - 1]):
     nums[i] -= p
     break
  return all(nums[i] > nums[i - 1] for i in range(1, len(nums)))