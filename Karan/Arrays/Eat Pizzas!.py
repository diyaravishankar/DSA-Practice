class Solution:
    def maxWeight(self, pizzas):
        pizzas.sort()
        n = len(pizzas)
        res = 0
        odd_days = (n // 4 + 1) // 2
        even_days = n // 4 - odd_days
        i = n
        while odd_days:
            i -= 1
            res += pizzas[i]
            odd_days -= 1
        while even_days:
            i -= 2
            res += pizzas[i]
            even_days -= 1
        return res