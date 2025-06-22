class Solution {
    static class pair{
        int node,wt;
        pair(int node,int wt){
            this.node=node;
            this.wt=wt;
        }
    }
    public int[] dijkstra(int V, int[][] edges, int src) {
        // code here
        List<List<pair>> adj=new ArrayList<>();
        for(int i=0;i<V;i++){
            adj.add(new ArrayList<>());
            
        }
        for(int edge[]:edges){
            int u=edge[0],v=edge[1],wt=edge[2];
            adj.get(u).add(new pair(v,wt));
            adj.get(v).add(new pair(u,wt));
        }
        int dist[]=new int[V];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;
        PriorityQueue<pair> pq=new PriorityQueue<>((a,b)->a.wt-b.wt);
        pq.offer(new pair(src, 0));
        while (!pq.isEmpty()) {
            pair current = pq.poll();
            int u = current.node;

            for (pair neighbor : adj.get(u)) {
                int v = neighbor.node;
                int wt = neighbor.wt;

                if (dist[u] + wt < dist[v]) {
                    dist[v] = dist[u] + wt;
                    pq.offer(new pair(v, dist[v]));
                }
            }
        }
        return dist;
    }
}