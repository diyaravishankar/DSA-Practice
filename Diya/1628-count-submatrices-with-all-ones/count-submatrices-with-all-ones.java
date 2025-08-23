class Solution {
    public int numSubmat(int[][] mat) {

        int count = 0;
        int[][] height = new int[mat.length][mat[0].length];
        for(int i = 0;i<mat[0].length;i++){
            height[0][i] = mat[0][i];
        }

        for(int i = 1;i<mat.length;i++){
            for(int j = 0;j<mat[0].length;j++){
                if(mat[i][j] == 1){
                    height[i][j] = 1 + height[i-1][j];
                }
                
            }
        }
       for(int i=0;i<height.length;i++){
        count += fcount(height[i]);
       }
       return count;

    }
    int fcount(int[] row){
         int col = row.length;
         int ans = 0;
         for(int i = 0;i<col;i++){
            if(row[i]!=0){
            int minh = row[i];
            for(int j = i;j>=0;j--){
              minh = Math.min(minh,row[j]);
              if(minh == 0){
                break;
              }
              ans+= minh;
            }
            }    
         }
         return ans;
    }
}











// class Solution {
//     public int numSubmat(int[][] mat) {
//         int row = mat.length;
//         int col = mat[0].length;
//         int count = 0;
//         for(int i = 0;i<row;i++){
//             for(int j=0;j<col;j++){
              
//               for(int k = i;k<row;k++){
//                 for(int l = j;l<col;l++ ){
//                      if(all1(mat,i,j,k,l)){
//                         count++;
//                      }
//                 }
//               }
//             }
//         }
//         return count;
//     }
//     boolean all1(int[][] mat,int row1,int col1,int row2,int col2){
//         for(int i = row1;i<=row2;i++){
//             for(int j = col1;j<=col2;j++){
//                 if(mat[i][j] == 0){
//                     return false;
//                 }
//             }
//         }
//         return true;
//     }
// }