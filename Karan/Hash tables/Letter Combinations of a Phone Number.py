class Solution:
 def letterCombinations(self, digits: str) -> list[str]:
  if not digits:
   return []
  digit_to_char = {
   "2": "abc",
   "3": "def",
   "4": "ghi",
   "5": "jkl",
   "6": "mno",
   "7": "pqrs",
   "8": "tuv",
   "9": "wxyz"
  }
  result = []
  def backtrack(index: int, path: list[str]):
   if index == len(digits):
    result.append("".join(path))
    return
   for letter in digit_to_char[digits[index]]:
    path.append(letter)
    backtrack(index + 1, path)
    path.pop()
  backtrack(0, [])
  return result