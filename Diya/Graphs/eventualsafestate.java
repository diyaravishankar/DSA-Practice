class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n];
        List<Integer> safeNodes = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (isSafe(i, graph, color)) {
                safeNodes.add(i);
            }
        }

        return safeNodes;

    }
    
    private static boolean isSafe(int node, int[][] graph, int[] color) {
        if (color[node] != 0) {
            return color[node] == 2; 
        }

        color[node] = 1; 

        for (int neighbor : graph[node]) {
            if (!isSafe(neighbor, graph, color)) {
                return false; /
            }
        }

        color[node] = 2;
        return true;
    }
}