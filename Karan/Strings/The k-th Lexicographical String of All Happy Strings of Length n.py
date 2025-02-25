class Solution:
 def getHappyString(self, n: int, k: int) -> str:
  def backtrack(curr):
   if len(curr) == n:
    result.append(curr)
    return
   for ch in "abc":
    if not curr or curr[-1] != ch:
     backtrack(curr + ch)
  result = []
  backtrack("")
  return result[k - 1] if k <= len(result) else ""
print(Solution().getHappyString(1, 3))
print(Solution().getHappyString(1, 4))
print(Solution().getHappyString(3, 9))