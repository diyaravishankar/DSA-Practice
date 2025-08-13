class Solution {
    public boolean isPowerOfThree(int n) {
        if(n==1) return true;
        for(int i=0;i<=Math.sqrt(n);i++){
        if(n%3==0 && Math.pow(3,i)==n) return true;
        }
        return false;

    }
}