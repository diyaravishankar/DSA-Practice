Shortest Path in Undirected Graph
# Problem: Given an undirected graph, find the shortest path between two nodes.


class Solution {
    // Function to find the shortest path from a source node to all other nodes
    public int[] shortestPath(ArrayList<ArrayList<Integer>> adj, int src) {
        // code here
         int n=adj.size();
        int dist[]=new int[n];
       
        for(int i=0;i<n;i++) dist[i]=Integer.MAX_VALUE;
        dist[src]=0;
        Queue<Integer> q=new LinkedList<>();
        q.add(src);
        while(!q.isEmpty()){
            Integer node=q.poll();
            for(int nbr:adj.get(node)){
                if(dist[node]+1<dist[nbr]){
                    dist[nbr]=1+dist[node];
                    q.add(nbr);
                }
            }
        }
        for(int i=0;i<n;i++){
            if(dist[i]==Integer.MAX_VALUE){
                dist[i]=-1;
            }
        }
        return dist;
    }
}
