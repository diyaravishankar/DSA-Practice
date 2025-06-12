// User function Template for Java

class Solution {
    public int maximumPoints(int[][] arr) {
        int n = arr.length;
        int[][] dp = new int[n][4];  // dp[day][lastTask]

        // Initialize with -1 (means uncomputed)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 4; j++) {
                dp[i][j] = -1;
            }
        }

        return helper(n - 1, 3, arr, dp);  // Start from last day, with no task done on previous day
    }

    private int helper(int day, int last, int[][] arr, int[][] dp) {
        if (dp[day][last] != -1) return dp[day][last];

        if (day == 0) {
            int max = 0;
            for (int task = 0; task < 3; task++) {
                if (task != last) {
                    max = Math.max(max, arr[0][task]);
                }
            }
            return dp[day][last] = max;
        }

        int maxPoints = 0;
        for (int task = 0; task < 3; task++) {
            if (task != last) {
                int points = arr[day][task] + helper(day - 1, task, arr, dp);
                maxPoints = Math.max(maxPoints, points);
            }
        }

        return dp[day][last] = maxPoints;
    }
}