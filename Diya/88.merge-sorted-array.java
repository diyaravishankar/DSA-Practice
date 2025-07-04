/*
 * @lc app=leetcode id=88 lang=java
 *
 * [88] Merge Sorted Array
 */

// @lc code=start
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int k=m;
        for(int i=0;i<n;i++){
            nums1[k]=nums2[i]; k++;
        }
        Arrays.sort(nums1);
    }
}
// @lc code=end

