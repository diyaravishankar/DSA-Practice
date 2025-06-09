class Solution {
    // Function to return a list containing the DFS traversal of the graph.
    public ArrayList<Integer> dfs(ArrayList<ArrayList<Integer>> adj) {
        // Code here
        int V=adj.size();
        boolean visited[]=new boolean[V];
        ArrayList<Integer> res=new ArrayList<>();
        dfshelper(0,visited,adj,res);
        return res;
        
    }
    public static void dfshelper(int node, boolean[] visited,ArrayList<ArrayList<Integer>> adj,ArrayList<Integer> res){
        visited[node]=true;
        res.add(node);
        for(int n:adj.get(node)){
            if(!visited[n]){
                dfshelper(n,visited,adj,res);
            }
        }
    }
}