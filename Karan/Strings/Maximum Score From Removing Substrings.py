class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s, first, second, points):
            stack = []
            score = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(ch)
            return ''.join(stack), score
        total = 0
        if x >= y:
            s, points_ab = remove_pair(s, 'a', 'b', x)
            _, points_ba = remove_pair(s, 'b', 'a', y)
        else:
            s, points_ba = remove_pair(s, 'b', 'a', y)
            _, points_ab = remove_pair(s, 'a', 'b', x)
        return points_ab + points_ba
