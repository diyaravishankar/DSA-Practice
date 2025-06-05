// User function Template for Java
import java.util.HashMap;

class Solution {
    static HashMap<String, Integer> memo;

    static int countWays(String s) {
        memo = new HashMap<>();
        return countWaysUtil(s, 0, s.length() - 1, true);
    }

    static int countWaysUtil(String s, int i, int j, boolean isTrue) {
        if (i > j) return 0;

        if (i == j) {
            if (isTrue) return s.charAt(i) == 'T' ? 1 : 0;
            else return s.charAt(i) == 'F' ? 1 : 0;
        }

        String key = i + "_" + j + "_" + isTrue;
        if (memo.containsKey(key)) return memo.get(key);

        int ans = 0;

        for (int k = i + 1; k <= j - 1; k += 2) {
            char operator = s.charAt(k);

            int lt = countWaysUtil(s, i, k - 1, true);
            int lf = countWaysUtil(s, i, k - 1, false);
            int rt = countWaysUtil(s, k + 1, j, true);
            int rf = countWaysUtil(s, k + 1, j, false);

            if (operator == '&') {
                if (isTrue) ans += lt * rt;
                else ans += lt * rf + lf * rt + lf * rf;
            } else if (operator == '|') {
                if (isTrue) ans += lt * rt + lt * rf + lf * rt;
                else ans += lf * rf;
            } else if (operator == '^') {
                if (isTrue) ans += lt * rf + lf * rt;
                else ans += lt * rt + lf * rf;
            }
        }

        memo.put(key, ans);
        return ans;
    }
}
