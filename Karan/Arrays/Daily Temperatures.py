class Solution:
    def dailyTemperatures(self, T):
        n = len(T)
        res = [0] * n
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res