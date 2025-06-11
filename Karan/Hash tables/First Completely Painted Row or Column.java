import java.util.*;
class Solution {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int m = mat.length, n = mat[0].length;
        Map<Integer, int[]> position = new HashMap<>();
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                position.put(mat[i][j], new int[]{i, j});
        int[] rowPaint = new int[m];
        int[] colPaint = new int[n];
        for (int i = 0; i < arr.length; i++) {
            int[] pos = position.get(arr[i]);
            int r = pos[0], c = pos[1];
            rowPaint[r]++;
            colPaint[c]++;
            if (rowPaint[r] == n || colPaint[c] == m)
                return i;
        }
        return -1; 
    }
}