class Solution {
    int maxAbsoluteSum(int[] nums) {
    int maxSum=0,minSum=0,currMax=0,currMin=0;
    for(int num:nums){
    currMax=Math.max(0,currMax+num);
    maxSum=Math.max(maxSum,currMax);
    currMin=Math.min(0,currMin+num);
    minSum=Math.min(minSum,currMin);
    }
    return Math.max(Math.abs(maxSum),Math.abs(minSum));
    }
    public static void main(String[] args) {
    Solution sol=new Solution();
    System.out.println(sol.maxAbsoluteSum(new int[]{1,-3,2,3,-4}));
    System.out.println(sol.maxAbsoluteSum(new int[]{2,-5,1,-4,3,-2}));
    }
    }