class Solution:
  def diffWaysToCompute(self, expression: str) -> list[int]:
    from functools import lru_cache
    @lru_cache(None)
    def compute(expr):
      res = []
      for i, ch in enumerate(expr):
        if ch in '+-*':
          left = compute(expr[:i])
          right = compute(expr[i+1:])
          for l in left:
            for r in right:
              if ch == '+': res.append(l + r)
              elif ch == '-': res.append(l - r)
              else: res.append(l * r)
      if not res: res.append(int(expr))
      return res
    return compute(expression)