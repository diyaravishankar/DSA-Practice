import java.util.*;

class Solution {
    public int minCost(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] cost = new int[m][n];
        for (int[] row : cost) Arrays.fill(row, Integer.MAX_VALUE);
        cost[0][0] = 0;
        Deque<int[]> dq = new ArrayDeque<>();
        dq.offer(new int[]{0, 0});
        int[][] dirs = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        while (!dq.isEmpty()) {
            int[] cell = dq.pollFirst();
            int r = cell[0], c = cell[1];
            for (int d = 0; d < 4; d++) {
                int nr = r + dirs[d][0];
                int nc = c + dirs[d][1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int newCost = cost[r][c] + (grid[r][c] == d + 1 ? 0 : 1);
                    if (newCost < cost[nr][nc]) {
                        cost[nr][nc] = newCost;
                        if (grid[r][c] == d + 1)
                            dq.addFirst(new int[]{nr, nc});
                        else
                            dq.addLast(new int[]{nr, nc});
                    }
                }
            }
        }
        return cost[m - 1][n - 1];
    }
}