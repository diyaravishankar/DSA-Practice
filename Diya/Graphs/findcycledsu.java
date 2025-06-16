public class DSUCycleDetection {

    static class DSU {
        int[] parent;

        DSU(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
        }

        // Find with path compression
        int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        // Union
        boolean union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);

            // If both nodes share the same root, a cycle exists
            if (rootX == rootY) return false;

            parent[rootY] = rootX; // merge sets
            return true;
        }
    }

    // Function to detect cycle
    static boolean hasCycle(int n, int[][] edges) {
        DSU dsu = new DSU(n);

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];

            if (!dsu.union(u, v)) {
                // Cycle detected
                return true;
            }
        }
        return false; // No cycles
    }

    public static void main(String[] args) {
        int n = 5; // Number of nodes
        int[][] edges = {
            {0, 1},
            {1, 2},
            {2, 3},
            {3, 4},
            {4, 0} // This edge creates a cycle
        };

        if (hasCycle(n, edges)) {
            System.out.println("Cycle detected!");
        } else {
            System.out.println("No cycle.");
        }
    }
}
