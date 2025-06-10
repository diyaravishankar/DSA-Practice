import java.util.*;

class Solution {
    public boolean wordBreak(String s, String[] wordDict) {
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;

        // Use HashSet for O(1) lookup
        Set<String> wordSet = new HashSet<>(Arrays.asList(wordDict));

        int max_len = 0;
        for (String word : wordDict) {
            max_len = Math.max(max_len, word.length());
        }

        for (int i = 1; i <= n; i++) {
            // Only check substrings of length up to max_len to optimize
            for (int j = i - 1; j >= Math.max(i - max_len, 0); j--) {
                if (dp[j] && wordSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n];
    }
}
