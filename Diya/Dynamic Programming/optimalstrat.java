
class Solution {
    public int maximumAmount(int arr[]) {
        int n = arr.length;
int[][] dp = new int[n][n];

// Base case: only one coin
for (int i = 0; i < n; i++) {
    dp[i][i] = arr[i];
}

// Base case: two coins — pick the max
for (int i = 0; i < n - 1; i++) {
    dp[i][i + 1] = Math.max(arr[i], arr[i + 1]);
}

// Fill the DP table for larger subarrays
for (int length = 2; length < n; length++) {
    for (int start = 0; start + length < n; start++) {
        int end = start + length;

        int pickStartNext1 = (start + 2 <= end) ? dp[start + 2][end] : 0;
        int pickStartNext2 = (start + 1 <= end - 1) ? dp[start + 1][end - 1] : 0;
        int pickEndNext1 = (start + 1 <= end - 1) ? dp[start + 1][end - 1] : 0;
        int pickEndNext2 = (start <= end - 2) ? dp[start][end - 2] : 0;

        int pickStart = arr[start] + Math.min(pickStartNext1, pickStartNext2);
        int pickEnd = arr[end] + Math.min(pickEndNext1, pickEndNext2);

        dp[start][end] = Math.max(pickStart, pickEnd);
    }
}
return(dp[0][n - 1]);

    }
}