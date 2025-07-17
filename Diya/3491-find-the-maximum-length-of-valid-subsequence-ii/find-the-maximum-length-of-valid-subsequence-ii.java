class Solution {
    public int maximumLength(int[] nums, int k) {
        int[][] dp = new int[k][k];
        int res=0;
        for(int num: nums){
            num%=k;
            for(int i=0; i<k; i++){
                dp[i][num]= dp[num][i]+1;
                res = Math.max(res, dp[i][num]);
            }
        }
        return res;
    }
}