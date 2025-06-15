    static class Pair {
        int node;
        int parent;
        
        Pair(int node, int parent) {
            this.node = node;
            this.parent = parent;
        }
    }
    public boolean isCycle(int V, int[][] edges) {
        // Code here
        boolean visited[]=new boolean[V];
        Arrays.fill(visited, false);
       for(int i=0;i<V;i++){
           if(visited[i]==false){
              if(checkforcycle(i,V,edges,visited))return true;
           }
       }
       return false;
    }
    public static boolean checkforcycle(int src,int V,int [][]edges,boolean[]visited){
        visited[src] = true;
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(src, -1));
        
        while(!q.isEmpty()) {
            Pair current = q.poll();
            int node = current.node;
            int parent = current.parent;
            
            // Find all neighbors of current node from edges array
            for(int[] edge : edges) {
                int neighbor = -1;
                
                // Check if current node is part of this edge
                if(edge[0] == node) {
                    neighbor = edge[1];
                } else if(edge[1] == node) {
                    neighbor = edge[0];
                }
                
                // If we found a neighbor
                if(neighbor != -1) {
                    if(!visited[neighbor]) {
                        visited[neighbor] = true;
                        q.add(new Pair(neighbor, node));
                    } else if(neighbor != parent) {
                        // If neighbor is visited and not parent, cycle found
                        return true;
                    }
                }
            }
        }
        return false;
    }
}