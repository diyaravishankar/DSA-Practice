class Solution {
    public List<Integer> luckyNumbers(int[][] matrix) {
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < matrix.length; i++) {
            int minVal = matrix[i][0];
            int colIdx = 0;

            for (int j = 1; j < matrix[0].length; j++) {
                if (matrix[i][j] < minVal) {
                    minVal = matrix[i][j];
                    colIdx = j;
                }
            }
            boolean isMaxInCol = true;
            for (int k = 0; k < matrix.length; k++) {
                if (matrix[k][colIdx] > minVal) {
                    isMaxInCol = false;
                    break;
                }
            }

            if (isMaxInCol) {
                result.add(minVal);
            }
        }

        return result;
    }
}
