class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int n = A.length;
        int[] res = new int[n];
        boolean[] seen = new boolean[n + 1];
        boolean[] inA = new boolean[n + 1];
        boolean[] inB = new boolean[n + 1];
        int common = 0;
        for (int i = 0; i < n; i++) {
            inA[A[i]] = true;
            inB[B[i]] = true;
            if (inA[B[i]] && !seen[B[i]]) {
                common++;
                seen[B[i]] = true;
            }
            if (inB[A[i]] && !seen[A[i]]) {
                common++;
                seen[A[i]] = true;
            }
            res[i] = common;
        }
        return res;
    }
}