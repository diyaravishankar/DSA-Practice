class Solution {
    public int findTheCity(int n, int[][] edges, int d) {
        // Initialize distance matrix with large values (infinity equivalent)
        int[][] dist = new int[n][n];
        int inf = (int)1e7;
        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], inf);
            dist[i][i] = 0;  // Distance to self is 0
        }

        // Fill in direct edge weights (undirected graph)
        for (int[] e : edges) {
            int u = e[0];
            int v = e[1];
            int c = e[2];
            dist[u][v] = c;
            dist[v][u] = c;
        }

        // Floyd-Warshall: update all-pairs shortest paths
        for (int v = 0; v < n; v++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    dist[i][j] = Math.min(dist[i][j],
                                          dist[i][v] + dist[v][j]);
                }
            }
        }

        // Find the city with the smallest number of reachable cities within distance 'd'
        int minReachable = inf;
        int ansNode = 0;
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (dist[i][j] <= d) {
                    count++;
                }
            }
            // Update if we find a city with a smaller count (or same count but larger index)
            if (count <= minReachable) {
                ansNode = i;
                minReachable = count;
            }
        }
        return ansNode;
    }
}