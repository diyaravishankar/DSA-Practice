class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        List<List<Integer>> graph=new ArrayList<>();
        boolean visited[]=new boolean[n];
        for(int i=0;i<n;i++){
            graph.add(new ArrayList<>());
        }
        for(int[] e:edges){
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }

        Queue<Integer> q=new LinkedList<>();
        q.add(source);
        while(!q.isEmpty()){
            int curr=q.poll();
            if(curr==destination){
                return true;
            }
            for(int nbr:graph.get(curr)){
                if (!visited[nbr]){
                    visited[nbr]=true;
                    q.add(nbr);
                }
            }
        }
        return false;
    }
}