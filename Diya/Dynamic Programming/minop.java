class Solution {
    public int minOperation(int n) {
        int[] dp = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            dp[i] = Integer.MAX_VALUE;
        }

        dp[1] = 0;

        for (int i = 1; i < n; i++) {
            if (i + 1 <= n) {
                dp[i + 1] = Math.min(dp[i + 1], dp[i] + 1);
            }
            if (i * 2 <= n) {
                dp[i * 2] = Math.min(dp[i * 2], dp[i] + 1);
            }
        }

        return dp[n]+1;
    }
}
