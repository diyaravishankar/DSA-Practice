class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
        current = 1
        for i in range(len(pattern) + 1):
            stack.append(current)
            current += 1
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result.append(str(stack.pop()))
        return ''.join(result)
solution = Solution()
print(solution.smallestNumber("IIIDIDDD"))
print(solution.smallestNumber("DDD"))
