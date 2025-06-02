// User function Template for Java

class Solution {

    public int minDifference(int arr[]) {
        int n=arr.length;
        sum=Arrays.stream(arr).sum();
        boolean dp=new boolean[n+1][sum+1];
        for(int i=0;i<=n;i++){
            dp[i][0]=true;
        }
        //subsetsum to find s1
        for (int i = 1; i <= n/2; i++) {
            for (int j = 1; j <= totalSum; j++) {
                if (arr[i - 1] <= j) {
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - arr[i - 1]];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        int minDiff = Integer.MAX_VALUE;
        for (int s1 = 0; s1 <= totalSum / 2; s1++) {
            if (dp[n][s1]) {
                int s2 = totalSum - s1;
                minDiff = Math.min(minDiff, Math.abs(s2 - s1));
            }
        }

        return minDiff;
    }
}
