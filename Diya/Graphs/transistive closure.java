// Floyd Warshall optimal
class Solution {
    static ArrayList<ArrayList<Integer>> transitiveClosure(int N, int graph[][]) {
        long [][] dist=new long[N][N];
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(graph[i][j]==1){
                    dist[i][j]=1;
                }
                else dist[i][j]=Integer.MAX_VALUE;
                if(i==j) dist[i][j]=0;
            }
            
        }
        for(int k=0;k<N;k++){
            for(int i=0;i<N;i++){
                for(int j=0;j<N;j++){
                    if(dist[i][j]>dist[k][j]+dist[i][k]) dist[i][j]=dist[k][j]+dist[i][k];
                }
            }
        }
       ArrayList<ArrayList<Integer>> ans = new ArrayList<>(N);
       for (int i = 0; i < N; i++) {
            ans.add(new ArrayList<>());
        }
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(dist[i][j]==Integer.MAX_VALUE){
                    ans.get(i).add(0);
                    
                }
                else{
                    ans.get(i).add(1);
                }
            }
        }
        return ans;
        
    }  
}

// DFS: not optimal
class Solution {
    static ArrayList<ArrayList<Integer>> transitiveClosure(int N, int graph[][]) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        int[][] tc = new int[N][N];
        for (int i = 0; i < N; i++) {
            dfs(i, i, graph, tc, N);
        }
        for (int i = 0; i < N; i++) {
            ArrayList<Integer> row = new ArrayList<>();
            for (int j = 0; j < N; j++) {
                row.add(tc[i][j]);
            }
            result.add(row);
        }

        return result;
    }
    static void dfs(int src, int curr, int[][] graph, int[][] tc, int N) {
        tc[src][curr] = 1;
        for (int i = 0; i < N; i++) {
            if (graph[curr][i] == 1 && tc[src][i] == 0) {
                dfs(src, i, graph, tc, N);
            }
        }
    }
}


