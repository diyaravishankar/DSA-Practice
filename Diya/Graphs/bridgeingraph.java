class Solution {
    int time;
    List<List<Integer>> adj;
    public boolean isBridge(int V, int[][] edges, int c, int d) {
        // code here
        time=0;
        adj=new ArrayList<>();
        for(int i=0;i<V;i++){
            adj.add(new ArrayList<>());
        }
        for(int edge[]:edges){
            int u=edge[0];int v=edge[1];
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        int disc[]=new int[V];
        int low[]=new int[V];
        boolean vis[]=new boolean[V];
        for(int i=0;i<V;i++){
            if(!vis[i]){
                if(dfs(i,-1,disc,low,vis,c,d)) return true;
            }
        }
        return false;
        
        
    }
    public boolean dfs(int u,int parent,int[] disc,int []low,boolean[] visited,int c,int d){
        visited[u] = true;
        disc[u] = low[u] = ++time;
        for (int v : adj.get(u)) {
            if (v == parent) continue;

            if (!visited[v]) {
                if (dfs(v, u, disc, low, visited, c, d)) return true;
                low[u] = Math.min(low[u], low[v]);

                // Check if (u, v) is a bridge
                if (low[v] > disc[u]) {
                    if ((u == c && v == d) || (u == d && v == c)) {
                        return true;
                    }
                }
            } else {
                low[u] = Math.min(low[u], disc[v]);
            }
        }
        return false;
    }
}