from collections import defaultdict
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i, n = 0, len(formula)
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i] or 1)
                top = stack.pop()
                for elem, cnt in top.items():
                    stack[-1][elem] += cnt * multiplier
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                elem = formula[start:i]
                start_count = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start_count:i] or 1)
                stack[-1][elem] += count
        result = ""
        for elem in sorted(stack[-1]):
            cnt = stack[-1][elem]
            result += elem + (str(cnt) if cnt > 1 else "")
        return result