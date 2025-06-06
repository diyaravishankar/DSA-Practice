public class LPSUsingReverse {
    // Function to compute LCS of two strings
    public static int lcs(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        int[][] dp = new int[n + 1][m + 1];

        // Build LCS table
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1))
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                else
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }

        return dp[n][m];
    }
    public static int longestPalindromicSubsequence(String s) {
        String reversed = new StringBuilder(s).reverse().toString();
        return lcs(s, reversed);  // LPS is LCS of s and reverse(s)
    }
}