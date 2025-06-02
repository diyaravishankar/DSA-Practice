class Solution {
    public int cutRod(int[] price) {
        int n=price.length;
        int length[]=new int[n];
        for(int i=0;i<n;i++){
            length[i]=i+1;
        }
        int dp[][]=new int[n+1][n+1];
        for(int i=0;i<n;i++){
            dp[0][i]=0;
            dp[i][0]=0;
        }
        int i=1;
        int j=1;
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
        if(length[i-1]<=j){
            dp[i][j]=Math.max(price[i-1]+dp[i][j-length[i-1]],dp[i-1][j]);
        }
        else{
            dp[i][j]=dp[i-1][j];
        }
        }
        }
        return dp[n][n];
    }
}