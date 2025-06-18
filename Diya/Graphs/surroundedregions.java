class Solution {
    public void solve(char[][] board) {
        //start from the boundary 0's and check how many other zeros are connected to boundary 0's
        int n=board.length;
        int m=board[0].length;
        boolean[][] visited=new boolean[n][m];
        //first row
        for(int j=0;j<m;j++){
                if(board[0][j]=='O' && !visited[0][j]){
                    dfs(board,0,j,visited);
                }
            }
        
        //first column
        for(int i=0;i<n;i++){
                if(board[i][0]=='O' && !visited[i][0]){
                    dfs(board,i,0,visited);
                }
            }
        
        //last row
        for(int j=0;j<m;j++){
                if(board[n-1][j]=='O' && !visited[n-1][j]){
                    dfs(board,n-1,j,visited);
                }
            }
        
         //right side column(last)
        for(int i=0;i<n;i++){
                if(board[i][m-1]=='O' && !visited[i][m-1]){
                    dfs(board,i,m-1,visited);
                }
            }
        

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(board[i][j]=='O'){
                    board[i][j]='X';
                } else if(board[i][j]=='#'){
                    board[i][j]='O';
                }
            }
        }
    }
    public static void dfs(char[][] board,int i,int j,boolean[][] visited){
        //make it visited
        visited[i][j]=true;
        board[i][j]='#';
        //for all its 4 directions call dfs so that 
        //it marks any boundary connected 0's
        int[] xD={-1,0,1,0};
        int[] yD={0,1,0,-1};
        for(int k=0;k<4;k++){
            int newRow=i+xD[k];
            int newCol=j+yD[k];
            if(newRow>=0 && newCol>=0 && newRow<board.length&& newCol<board[0].length&&!visited[newRow][newCol]&&
            board[newRow][newCol]=='O'){
                dfs(board,newRow,newCol,visited);
            }
        }
        }
}