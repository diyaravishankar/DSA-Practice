import heapq
class Solution:
  def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
    uglies = [1]
    heap = [(p, p, 0) for p in primes]
    heapq.heapify(heap)
    while len(uglies) < n:
      val, prime, idx = heapq.heappop(heap)
      if val != uglies[-1]:
        uglies.append(val)
      heapq.heappush(heap, (prime * uglies[idx + 1], prime, idx + 1))
    return uglies[-1]