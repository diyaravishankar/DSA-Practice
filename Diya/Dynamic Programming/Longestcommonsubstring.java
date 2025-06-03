class Solution {
    public int longestCommonSubstr(String s1, String s2) {
        int m=s1.length();
        int n=s2.length();
        int res=0;
        int [][]dp=new int[m+1][n+1];
        for(int i=0;i<=m;i++){
                for(int j=0;j<=n;j++){
                    if(i==0||j==0){
                        dp[i][j]=0;
                    }
                    else{
                        if(s1.charAt(i-1)==s2.charAt(j-1)){
                            dp[i][j]=1+dp[i-1][j-1];
                            res=Math.max(dp[i][j],res);
                        }
                        else{
                            dp[i][j]=0;
                        }
                    }
                }
            }
            return res;
    }
}