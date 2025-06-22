class Solution:
 def solveSudoku(self, board: list[list[str]]) -> None:
  rows = [set() for _ in range(9)]
  cols = [set() for _ in range(9)]
  boxes = [set() for _ in range(9)]
  for r in range(9):
   for c in range(9):
    val = board[r][c]
    if val != '.':
     rows[r].add(val)
     cols[c].add(val)
     boxes[(r // 3) * 3 + (c // 3)].add(val)
  def backtrack(r: int, c: int) -> bool:
   if r == 9:
    return True
   if c == 9:
    return backtrack(r + 1, 0)
   if board[r][c] != '.':
    return backtrack(r, c + 1)
   for ch in '123456789':
    box_idx = (r // 3) * 3 + (c // 3)
    if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box_idx]:
     board[r][c] = ch
     rows[r].add(ch)
     cols[c].add(ch)
     boxes[box_idx].add(ch)
     if backtrack(r, c + 1):
      return True
     board[r][c] = '.'
     rows[r].remove(ch)
     cols[c].remove(ch)
     boxes[box_idx].remove(ch)
   return False
  backtrack(0, 0)