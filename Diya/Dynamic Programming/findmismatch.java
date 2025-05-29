class Solution {
    public int minOperations(String s1, String s2, int x) {
        int mismatch = 0;
        List<Integer> pos = new ArrayList<>();

        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                mismatch++;
                pos.add(i);
            }

        }
        if (mismatch%2 != 0) return -1;
        float[] dp = new float[mismatch];
        
        int[] poses = new int[mismatch];
        for (int i = 0; i < mismatch; i++) {
            poses[i] = pos.get(i);
        }
        return (int)helper(dp, poses, 0, x);
    }
    private float helper(float[] dp, int[] pos, int curPos, int x) {
        if (curPos >= pos.length) return 0; 
        if (dp[curPos] != 0) return dp[curPos];

        //take out two adjacencies
        float curCost = Integer.MAX_VALUE;
        if (curPos + 1 < pos.length) curCost = Math.min(curCost, pos[curPos + 1] - pos[curPos] + helper(dp, pos, curPos + 2, x));
        curCost = Math.min(curCost, (float)x/2 + helper(dp, pos, curPos + 1, x));

        return dp[curPos] = curCost;
    }
}