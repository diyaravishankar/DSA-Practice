class Solution:
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        i = j = count = 0
        n, m = len(players), len(trainers)
        while i < n and j < m:
            if players[i] <= trainers[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count