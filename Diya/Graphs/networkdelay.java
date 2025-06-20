class Solution {

    // Pair class to represent a neighbor and the time to reach it
    class Pair {
        int u; // Node number
        int t; // Time to reach this node

        public Pair(int u, int t) {
            this.u = u;
            this.t = t;
        }
    }

    List<List<Pair>> g; // Adjacency list

    public int networkDelayTime(int[][] times, int n, int k) {
        // Step 1: Build the graph
        g = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            g.add(new ArrayList<>()); // Initialize adjacency list for each node
        }

        // Populate the graph with edges (convert to 0-indexed)
        for (int[] e : times) {
            int u = e[0] - 1; // 0-indexed node
            int v = e[1] - 1; // 0-indexed neighbor
            int t = e[2];     // time to reach
            g.get(u).add(new Pair(v, t));
        }

        // Step 2: Initialize distance array to "infinity"
        int[] dist = new int[n];
        Arrays.fill(dist, (int)1e9);
        dist[k - 1] = 0; // Distance to source node is 0

        // Step 3: BFS-style traversal to relax edges
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(k - 1, 0)); // Start from the source

        while (!q.isEmpty()) {
            Pair node = q.poll(); // Get current node
            int minToReachNode = node.t; // Time to reach this node
            int u = node.u;

            // Explore all neighbors
            for (Pair child : g.get(u)) {
                // If a shorter path to neighbor is found, update it and add to queue
                if (minToReachNode + child.t < dist[child.u]) {
                    dist[child.u] = minToReachNode + child.t;
                    q.add(new Pair(child.u, minToReachNode + child.t));
                }
            }
        }

        // Step 4: Find the maximum distance to any reachable node
        int max = -1;
        for (int x : dist) {
            if (x == (int)1e9) {
                return -1; // Some node is unreachable
            }
            max = Math.max(max, x); // Keep track of the maximum time
        }

        return max;
    }
}