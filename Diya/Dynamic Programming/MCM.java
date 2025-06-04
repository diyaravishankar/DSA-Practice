class Solution {
    static int matrixMultiplication(int arr[]) {
        // code here
        int n = arr.length;
        int[][] dp = new int[n][n];

        // Initialize all values to -1
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], -1);
        }

        return solve(arr,dp, 1, n - 1);
    }

    static int solve(int[] arr,int[][] dp, int i, int j) {
        if (i >= j) return 0;

        if (dp[i][j] != -1)
            return dp[i][j];

        int min = Integer.MAX_VALUE;

        for (int k = i; k < j; k++) {
            int tempAns = solve(arr,dp, i, k)
                        + solve(arr, dp,k + 1, j)
                        + arr[i - 1] * arr[k] * arr[j];

            if (tempAns < min)
                min = tempAns;
        }

        dp[i][j] = min;
        return dp[i][j];
    }
}