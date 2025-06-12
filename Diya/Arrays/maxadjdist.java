class Solution {
    public int maxAdjacentDistance(int[] nums) {
        int d=Integer.MIN_VALUE;
        for(int num=0;num<nums.length-1;num++){
            d=Math.max(d,Math.abs(nums[num]-nums[num+1]));
        }
        return d>Math.abs(nums[0]-nums[nums.length-1])?d:Math.abs(nums[0]-nums[nums.length-1]);
    }
}