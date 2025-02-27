class Solution {
    boolean canJump(int[] nums) {
    int maxReach=0;
    for(int i=0;i<nums.length;i++){
    if(i>maxReach)return false;
    maxReach=Math.max(maxReach,i+nums[i]);
    if(maxReach>=nums.length-1)return true;
    }
    return true;
    }
    public static void main(String[] args) {
    Solution sol=new Solution();
    System.out.println(sol.canJump(new int[]{2,3,1,1,4}));
    System.out.println(sol.canJump(new int[]{3,2,1,0,4}));
    }
    }