class Solution {
    public int boxDelivering(int[][] A, int portsCount, int m1, int m2) {
        int n = A.length;
        boolean[] C = new boolean[n];
        for (int i = 0; i< n-1; i++){
            if (A[i][0] != A[i+1][0]) C[i] = true;
        }
        int[] dp = new int[n+1];
        int sum = 0; 
        int start = 0; 
        int diff = 0; 
        for (int i = 0; i< n; i++){
            if (i-start == m1) {
                sum-= A[start][1];
                if (C[start]) diff--;
                start++;
            }
            sum+= A[i][1];
            if (i> 0 && C[i-1]) diff++;
            while (sum > m2){
                sum-= A[start][1];
                if (C[start]) diff--;
                start++;
            }
            while(start < i && dp[start] == dp[start+1]){
                sum-= A[start][1];
                if (C[start]) diff--;
                start++;
            }
            
            dp[i+1] = diff+2 + dp[start];
        }
        return dp[n];
    }
}