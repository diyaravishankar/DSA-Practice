class Solution {
    static int knapsack(int W, int val[], int wt[]) {
        // code here
        int n=wt.length;
        int [][]dp=new int[n+1][W+1];
        for(int i=0;i<=n;i++){
            for(int j=0;j<=W;j++){
                if(i==0||j==0) dp[i][j]=0;
                else{
                    if(wt[i-1]<=j){
                        dp[i][j]=Math.max(dp[i-1][j],val[i-1]+dp[i-1][j-wt[i-1]]);
                    }
                    else{
                        dp[i][j]=dp[i-1][j];
                    }
                }
            }
        }
        return dp[n][W];
    }
}