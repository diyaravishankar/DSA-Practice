class Solution {
    int time;
    int[] dist, low;
    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        dist = new int[n];
        low = new int[n];
        int[] count = new int[n];
        for (List<Integer> c: connections) {
            count[c.get(0)]++;
            count[c.get(1)]++;
        }
        int[][] graph = new int[n][];
        for (int i=0; i<n; i++) {
            graph[i] = new int[count[i]];
        }
        for (List<Integer> c: connections) {
            int a = c.get(0);
            int b = c.get(1);
            graph[a][--count[a]] = b;
            graph[b][--count[b]] = a;
        }
        List<List<Integer>> result = new ArrayList<>();
        int time = 1;
        traverse(0, graph, result, -1);
        return result;
    }
    private void traverse(int node, int[][] graph, List<List<Integer>> result, int prev) {
        dist[node] = low[node] = time++;
        for (int next : graph[node]) {
            if (next == prev) continue;
            if (low[next] == 0) {
                traverse(next, graph, result, node);
                low[node] = Math.min(low[node], low[next]);
                if (dist[node] < low[next]) result.add(Arrays.asList(node, next));
            } else {
                low[node] = Math.min(low[node], low[next]);
            }
        }
    }
}