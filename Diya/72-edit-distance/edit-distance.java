class Solution {
    public int minDistance(String word1, String word2) {
        int n = word1.length(), m = word2.length();
        // Depicts the previous row
        int[] dp = new int[n + 1];
        
        for (int i = 0; i <= n; i++) {
            dp[i] = i;
        }

        for (int i = 1; i <= m; i++) {
            // Current row
            int[] curr = new int[n + 1];
            curr[0] = i;
            
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(j - 1) == word2.charAt(i - 1)) {
                    curr[j] = dp[j - 1];
                } else {
                    curr[j] = 1 + Math.min(dp[j], Math.min(dp[j - 1], curr[j - 1]));
                }
            }
            dp = curr;
        }
        return dp[n];
    }
}