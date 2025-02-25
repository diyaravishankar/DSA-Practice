class Solution:
    def mostProfitablePath(self, edges, bob, amount):
        from collections import defaultdict
        self.tree = defaultdict(list)
        for u, v in edges:
            self.tree[u].append(v)
            self.tree[v].append(u)
        self.bob_time = {}
        self.max_profit = float('-inf')
        self.find_bob_path(bob, -1, 0)
        self.dfs_alice(0, -1, 0, 0, amount)
        return self.max_profit
    def find_bob_path(self, node, parent, time):
        if node == 0:
            self.bob_time[node] = time
            return True
        for neighbor in self.tree[node]:
            if neighbor != parent:
                if self.find_bob_path(neighbor, node, time + 1):
                    self.bob_time[node] = time
                    return True
        return False
    def dfs_alice(self, node, parent, time, profit, amount):
        if node in self.bob_time:
            if self.bob_time[node] > time:
                profit += amount[node]
            elif self.bob_time[node] == time:
                profit += amount[node] // 2
        else:
            profit += amount[node]
        if len(self.tree[node]) == 1 and node != 0:
            self.max_profit = max(self.max_profit, profit)
            return
        for neighbor in self.tree[node]:
            if neighbor != parent:
                self.dfs_alice(neighbor, node, time + 1, profit, amount)