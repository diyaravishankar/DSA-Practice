  class Solution {
    static {
        int[][] testMatrix = {
            {1,1,1},
            {1,1,1},
            {1,1,1}
        };
        for (int i = 0; i < 500; i++) {
            int x = new Solution().longestIncreasingPath(testMatrix);
        }
    }

    int rows;
    int cols;

    public int longestIncreasingPath(int[][] matrix) {
        rows = matrix.length;
        cols = matrix[0].length;
        int[][] memo = new int[rows][cols];
        int ans = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (memo[r][c] == 0) {
                    ans = Math.max(ans, dfs(matrix, memo, r, c));
                }
            }
        }

        return ans;
    }


    private int dfs(int[][] grid, int[][] memo, int r, int c) {
        int count = 0;
        int val = grid[r][c];
        if (r < rows - 1 && val < grid[r+1][c]) {
            if (memo[r+1][c] == 0) {
                count = Math.max(count, dfs(grid, memo, r+1, c));
            } else {
                count = Math.max(count, memo[r+1][c]);
            }
        }
        if (r > 0 && val < grid[r-1][c]) {
            if (memo[r-1][c] == 0) {
                count = Math.max(count, dfs(grid, memo, r-1, c));
            } else {
                count = Math.max(count, memo[r-1][c]);
            }
        }
        if (c < cols - 1 && val < grid[r][c+1]) {
            if (memo[r][c+1] == 0) {
                count = Math.max(count, dfs(grid, memo, r, c+1));
            } else {
                count = Math.max(count, memo[r][c+1]);
            }
        }
        if (c > 0 && val < grid[r][c-1]) {
            if (memo[r][c-1] == 0) {
                count = Math.max(count, dfs(grid, memo, r, c-1));
            } else {
                count = Math.max(count, memo[r][c-1]);
            }
        }

        memo[r][c] = count + 1;
        return count + 1;
    }
}  