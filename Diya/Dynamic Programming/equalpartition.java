class Solution {
    static boolean equalPartition(int arr[]) {
        // code here
    int n = arr.length;
    
    int sum=Arrays.stream(arr).sum();
    if (sum % 2 != 0) {
            return false;
        }

    int target = sum / 2;
    boolean[][] dp = new boolean[n + 1][target + 1];
    for (int i = 0; i <= n; i++) {
        dp[i][0] = true;
    }
    for (int j = 1; j <= target; j++) {
        dp[0][j] = false;
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= target; j++) {
            if (arr[i - 1] <= j) {
                dp[i][j] = dp[i - 1][j - arr[i - 1]] || dp[i - 1][j];
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    return dp[n][target];
    }
}