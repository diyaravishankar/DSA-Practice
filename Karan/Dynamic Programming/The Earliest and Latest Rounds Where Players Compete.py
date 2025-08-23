class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        def dfs(players):
            l, r = 0, len(players) - 1
            while l < r:
                if (players[l] == firstPlayer and players[r] == secondPlayer) or \
                   (players[l] == secondPlayer and players[r] == firstPlayer):
                    return (1, 1)
                l += 1
                r -= 1
            next_round = set()
            l, r = 0, len(players) - 1
            while l < r:
                a, b = players[l], players[r]
                if {a, b} & {firstPlayer, secondPlayer}:
                    if a in {firstPlayer, secondPlayer}:
                        next_round.add(a)
                    else:
                        next_round.add(b)
                else:
                    next_round.add((a, b))
                l += 1
                r -= 1
            if l == r:
                next_round.add(players[l])
            results = []
            def expand(index, current):
                if index == len(next_round):
                    results.append(sorted(current))
                    return
                item = list(next_round)[index]
                if isinstance(item, tuple):
                    expand(index + 1, current + [item[0]])
                    expand(index + 1, current + [item[1]])
                else:
                    expand(index + 1, current + [item])
            expand(0, [])
            min_round, max_round = float('inf'), float('-inf')
            for nxt in results:
                er, lr = dfs(nxt)
                min_round = min(min_round, er + 1)
                max_round = max(max_round, lr + 1)
            return (min_round, max_round)
        players = list(range(1, n + 1))
        return list(dfs(players))