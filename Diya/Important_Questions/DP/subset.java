class Solution {

    static Boolean isSubsetSum(int arr[], int sum) {
        // code here
        int k=arr.length;
        boolean dp[][]=new boolean[k+1][sum+1];
        for(int j=0;j<sum+1;j++){
            dp[0][j]=false;
        }
        for(int i=0;i<=k;i++){
            dp[i][0]=true;
        }
        for(int i=1;i<=k;i++){
            for(int j=1;j<=sum;j++){
                if(arr[i-1]<=j){
                    dp[i][j]=dp[i-1][j-arr[i-1]]||dp[i-1][j];
                }
                else{
                    dp[i][j]=dp[i-1][j];
                }
            }
        }
        return dp[k][sum];
    }
}