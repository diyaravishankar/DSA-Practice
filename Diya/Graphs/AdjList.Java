import java.util.*;

class Solution {
    public List<List<Integer>> printGraph(int V, int[][] edges) {
        List<Integer>[] adj = new ArrayList[V];
        for (int i = 0; i < V; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            adj[u].add(v);
            adj[v].add(u);
        }

        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            result.add(adj[i]);
        }
        return result;
    }
}
