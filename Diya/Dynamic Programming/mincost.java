class Solution {
    int minCost(int[] height) {
        // code here
        int n=height.length;
        if (n == 0 || n == 1) {
            return 0;
        }
        int []dp=new int[n+1];
        dp[0] = 0;
        dp[1] = Math.abs(height[1] - height[0]);
        
         for (int i = 2; i < n; i++) {
            int oneStep = dp[i - 1] + Math.abs(height[i] - height[i - 1]);
            int twoSteps = dp[i - 2] + Math.abs(height[i] - height[i - 2]);
            dp[i] = Math.min(oneStep, twoSteps);
        }
        return dp[n-1];
    }
}