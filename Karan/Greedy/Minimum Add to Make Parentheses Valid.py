class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        moves = 0
        for c in s:
            if c == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    moves += 1
        return moves + balance
sol = Solution()
print(sol.minAddToMakeValid("())"))
print(sol.minAddToMakeValid("((("))