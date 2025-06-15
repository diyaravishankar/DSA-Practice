class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n=triangle.size();
        Integer[][] memo = new Integer[n][n];
        return dfs(0, 0,triangle, memo);
    }
    public static int dfs(int i,int j,List<List<Integer>> triangle, Integer[][] memo){
        if(i==triangle.size()-1){
            return triangle.get(i).get(j);
        }
        if(memo[i][j]!=null){
            return memo[i][j];
        }
        int left=dfs(i+1,j,triangle,memo);
        int right=dfs(i+1,j+1,triangle,memo);
        memo[i][j]=triangle.get(i).get(j)+Math.min(left,right);
        return memo[i][j];
    }
}