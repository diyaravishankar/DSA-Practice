class Solution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        int n=fruits.length;
        int res=n;
        for(int i=0;i<n;i++){
            for(int j=0; j<n; j++){
                if(fruits[i]<=baskets[j]) {
                    res--;
                    baskets[j]=0;
                    break;
                }
            } 
        }
        return res;
    }
}