import java.util.*;

public class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return 0;

        int rows = matrix.length, cols = matrix[0].length;
        int[][] indegree = new int[rows][cols];
        int[][] directions = {{-1,0}, {1,0}, {0,-1}, {0,1}};

        // Step 1: Compute in-degree for each cell
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                for (int[] dir : directions) {
                    int ni = i + dir[0];
                    int nj = j + dir[1];
                    if (ni >= 0 && ni < rows && nj >= 0 && nj < cols && matrix[ni][nj] > matrix[i][j]) {
                        indegree[ni][nj]++;
                    }
                }
            }
        }

        // Step 2: Add all nodes with in-degree 0 to queue
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (indegree[i][j] == 0) {
                    queue.offer(new int[]{i, j});
                }
            }
        }

        // Step 3: BFS (Topological Sort)
        int pathLength = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            pathLength++;  // Each level represents an increase in path length

            for (int k = 0; k < size; k++) {
                int[] cell = queue.poll();
                int i = cell[0], j = cell[1];

                for (int[] dir : directions) {
                    int ni = i + dir[0];
                    int nj = j + dir[1];

                    if (ni >= 0 && ni < rows && nj >= 0 && nj < cols && matrix[ni][nj] > matrix[i][j]) {
                        indegree[ni][nj]--;
                        if (indegree[ni][nj] == 0) {
                            queue.offer(new int[]{ni, nj});
                        }
                    }
                }
            }
        }

        return pathLength;
    }
}