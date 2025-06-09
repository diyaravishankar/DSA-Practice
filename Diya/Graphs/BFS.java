class Solution {
    // Function to return Breadth First Search Traversal of given graph.
    public ArrayList<Integer> bfs(ArrayList<ArrayList<Integer>> adj) {
        // code here
        int V=adj.size();
        ArrayList<Integer> res=new ArrayList<>();
        Queue<Integer> q=new LinkedList<>();
        boolean visited[]=new boolean[V];
        int s=0;
        visited[s]=true;
        q.add(s);
        while(!q.isEmpty()){
            int curr=q.poll();
            res.add(curr);
            for(int x:adj.get(curr)){
                if(!visited[x]){
                    visited[x]=true;
                    q.add(x);
                }
            }
            
        }
        return res;
    }
}