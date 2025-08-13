class Solution {
    private static final int MOD = 1_000_000_007;
    private int[][] cache;
    private int n;
    private int x;
    
    public int numberOfWays(int n, int x) {
        this.n = n;
        this.x = x;
        this.cache = new int[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                cache[i][j] = -1;
            }
        }
        return backtrack(1, 0);
    }
    
    private int backtrack(int num, int total) {
        if (total > n) return 0;
        if (total == n) return 1;
        int current = (int) Math.pow(num, x);
        if (current > n) return 0;
        if (cache[num][total] != -1) return cache[num][total];
        cache[num][total] = (backtrack(num + 1, total + current) + backtrack(num + 1, total)) % MOD;
        return cache[num][total];
    }
}