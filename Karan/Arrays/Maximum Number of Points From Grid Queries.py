from heapq import heappush, heappop
class Solution:
    def maxPoints(self, grid, queries):
        m, n = len(grid), len(grid[0])
        queries = sorted((q, i) for i, q in enumerate(queries))
        res = [0] * len(queries)
        heap, visited, count = [(grid[0][0], 0, 0)], set([(0, 0)]), 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for q, i in queries:
            while heap and heap[0][0] < q:
                val, r, c = heappop(heap)
                count += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        heappush(heap, (grid[nr][nc], nr, nc))
                        visited.add((nr, nc))
            res[i] = count
        return res