class Solution {

    public int minCoins(int coins[], int amount) {
        // code here
        int n = coins.length;
        int[] dp = new int[amount + 1];

        Arrays.fill(dp, (int)1e9); // Use a very large value to simulate infinity
        dp[0] = 0; // Base case: 0 coins needed to make amount 0

        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i - coin >= 0) {
                    dp[i] = Math.min(dp[i], 1 + dp[i - coin]);
                }
            }
        }

        return dp[amount] == (int)1e9 ? -1 : dp[amount];
    }
}