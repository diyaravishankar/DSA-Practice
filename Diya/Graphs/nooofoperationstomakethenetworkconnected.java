class Solution {
    class DSU {
        int[] parent, rank;

        DSU(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }

        int find(int x) {
            if (parent[x] != x)
                parent[x] = find(parent[x]);
            return parent[x];
        }

        boolean union(int x, int y) {
            int px = find(x), py = find(y);
            if (px == py) return false;

            if (rank[px] < rank[py]) parent[px] = py;
            else if (rank[py] < rank[px]) parent[py] = px;
            else {
                parent[py] = px;
                rank[px]++;
            }
            return true;
        }
    }

    public int makeConnected(int n, int[][] connections) {
        if (connections.length < n - 1) return -1; // Not enough cables

        DSU dsu = new DSU(n);
        int components = n;

        for (int[] edge : connections) {
            if (dsu.union(edge[0], edge[1])) {
                components--; // Two nodes connected, reduce component count
            }
        }

        return components - 1;
    }
}