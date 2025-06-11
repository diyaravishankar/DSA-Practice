class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int m=matrix.length;
        int n=matrix[0].length;
        Integer memo[][]=new Integer[m][n];
        int minSum = Integer.MAX_VALUE;
        for (int j = 0; j < n; j++) {
            minSum = Math.min(minSum, dfs(0, j, matrix, memo));
        }
        return minSum;
    }
    public int dfs(int i,int j,int [][]matrix,Integer[][] memo){
        
        if (j < 0 || j >= matrix[0].length) return Integer.MAX_VALUE;
        if (i == matrix.length- 1) return matrix[i][j];
        if(memo[i][j]!=null){ return memo[i][j];}
        int next=dfs(i+1,j-1,matrix,memo);
        int down=dfs(i+1,j,matrix,memo);
        int diag=dfs(i+1,j+1,matrix,memo);
        memo[i][j]=matrix[i][j]+Math.min(diag,Math.min(next,down));
        return memo[i][j];
    }
}