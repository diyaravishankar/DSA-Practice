class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        min_balance = 0
        for c in s:
            if c == '[':
                balance += 1
            else:
                balance -= 1
            min_balance = min(min_balance, balance)
        return (-min_balance + 1) // 2
sol = Solution()
print(sol.minSwaps("][]["))
print(sol.minSwaps("]]][[["))
print(sol.minSwaps("[]"))