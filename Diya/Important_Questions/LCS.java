//Topdown-Memoization
import java.util.*;

class Solution {
    static int lcs(String s1, String s2) {
        // code here
        int m=s1.length();
        int n=s2.length();
        int [][]dp=new int[m+1][n+1];
        for(int i=0;i<=m;i++){
                for(int j=0;j<=n;j++){
                    if(i==0||j==0){
                        dp[i][j]=0;
                    }
                    else{
                        if(s1.charAt(i-1)==s2.charAt(j-1)){
                            dp[i][j]=1+dp[i-1][j-1];
                        }
                        else{
                            dp[i][j]=Math.max(dp[i-1][j],dp[i][j-1]);
                        }
                    }
                }
            }
            return dp[m][n];
        
    }
}

//bottomup 
public class LCS_BottomUp {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();
        int[][] dp = new int[m + 1][n + 1];

        // Fill dp table
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (text1.charAt(i) == text2.charAt(j)) {
                    dp[i][j] = 1 + dp[i + 1][j + 1];
                } else {
                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j + 1]);
                }
            }
        }
        return dp[0][0];
    }
}

// Recursive
public class LCS_Recursive {
    public int longestCommonSubsequence(String text1, String text2) {
        return lcs(text1, text2, 0, 0);
    }

    private int lcs(String s1, String s2, int i, int j) {
        if (i == s1.length() || j == s2.length())
            return 0;
        if (s1.charAt(i) == s2.charAt(j)) {
            return 1 + lcs(s1, s2, i + 1, j + 1);
        } else {
            return Math.max(lcs(s1, s2, i + 1, j), lcs(s1, s2, i, j + 1));
        }
    }
}
