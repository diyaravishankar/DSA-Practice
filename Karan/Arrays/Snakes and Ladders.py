from collections import deque
class Solution:
 def snakesAndLadders(self, board: list[list[int]]) -> int:
  n = len(board)
  def get_coordinates(square: int) -> tuple[int, int]:
   row = (square - 1) // n
   col = (square - 1) % n
   actual_row = n - 1 - row
   actual_col = col if row % 2 == 0 else n - 1 - col
   return actual_row, actual_col
  visited = set()
  queue = deque()
  queue.append((1, 0))
  while queue:
   square, moves = queue.popleft()
   for i in range(1, 7):
    next_square = square + i
    if next_square > n * n:
     continue
    r, c = get_coordinates(next_square)
    if board[r][c] != -1:
     next_square = board[r][c]
    if next_square == n * n:
     return moves + 1
    if next_square not in visited:
     visited.add(next_square)
     queue.append((next_square, moves + 1))
  return -1