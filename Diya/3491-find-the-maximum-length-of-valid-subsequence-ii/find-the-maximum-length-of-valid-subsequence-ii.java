class Solution {
    public int maximumLength1(int[] A, int k1) {
        int res = 0, k = k1, dp[][] = new int[k][k];
        for (int a : A) {
            for (int b = 0; b < k; b++) {
                //dp[a%k][b] - dp[b][a%k]
                //same reminder can be only extended with same reminder numbers [b]
                //And we have to maintain subsequence for different reminders from starting a%k
                dp[b][a % k] = dp[a % k][b] + 1;
                res = Math.max(res, dp[b][a % k]);
            }
        }
        return res;
    }

        public int maximumLength(int[] A, int k) {
        int res = 0;
        for (int v = 0; v < k; v++) {
            int[] dp = new int[k];
            for (int a : A) {
                dp[a % k] = dp[(v + k - a % k) % k] + 1;
                res = Math.max(res, dp[a % k]);
            }
        }
        return res;
    }
}