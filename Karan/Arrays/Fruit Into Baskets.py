from collections import defaultdict
class Solution:
    def totalFruit(self, fruits):
        fruit_count = defaultdict(int)
        start = max_fruits = 0
        for end in range(len(fruits)):
            fruit_count[fruits[end]] += 1
            while len(fruit_count) > 2:
                fruit_count[fruits[start]] -= 1
                if fruit_count[fruits[start]] == 0:
                    del fruit_count[fruits[start]]
                start += 1
            max_fruits = max(max_fruits, end - start + 1)
        return max_fruits