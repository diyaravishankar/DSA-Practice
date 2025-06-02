
class Solution {
    int countPartitions(int[] arr, int d) {
        int totalsum=Arrays.stream(arr).sum();
        if ((totalsum + d) % 2 != 0 || totalsum < d){ return 0;}
        int sum = (d + totalsum) / 2;
        return countsubsetsum(arr,sum);
    }
    int countsubsetsum(int [] arr,int sum){
        int n=arr.length;
        int [][]dp=new int[n+1][sum+1];
        for(int i=0;i<=n;i++){
            dp[i][0]=1;
        }
        for(int i=1;i<=n;i++){
            for(int j=0;j<=sum;j++){
                if(arr[i-1]<=j){
                    dp[i][j]=dp[i-1][j-arr[i-1]]+dp[i-1][j];
                }
                else{
                    dp[i][j]=dp[i-1][j];
                }
            }
        }
        return dp[n][sum];
    }
}
