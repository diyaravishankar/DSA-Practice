class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int m=mat.length;
        int n=mat[0].length;
        int dist[][]=new int[m][n];
        Queue <int[]> q=new LinkedList<>();
        boolean visited[][]=new boolean[m][n];
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(mat[i][j]==0){
                    dist[i][j]=0;
                    visited[i][j]=true;
                    q.offer(new int[]{i,j});
                }
            }
        }
        int[][] dir={{0,1},{1,0},{-1,0},{0,-1}};
        while(!q.isEmpty()){
            int cell[]=q.poll();
            int row = cell[0];
            int col = cell[1];
            for(int[] d : dir ){
                int r = row +d[0]; int c = col + d[1];
                if(r >=0 && r< m && c>=0 && c<n && !visited[r][c]){
                    dist[r][c] = dist[row][col] + 1;
                    visited[r][c] = true;
                    q.offer(new int[]{r, c});
                }
            }
        }
        return dist;
    }
}