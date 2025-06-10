class Solution {
    static int lis(int arr[]) {
        int n = arr.length;
        int[] dp = new int[n];
        
        // Each element is at least part of a subsequence of length 1
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        // Return the max LIS length from all dp[i]
        int maxLen = 0;
        for (int len : dp) {
            maxLen = Math.max(maxLen, len);
        }
        return maxLen;
    }
}
