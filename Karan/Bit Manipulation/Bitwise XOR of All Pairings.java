class Solution {
    public int xorAllNums(int[] nums1, int[] nums2) {
        int xor1 = 0, xor2 = 0;
        for (int x : nums1) xor1 ^= x;
        for (int y : nums2) xor2 ^= y;
        int res = 0;
        if (nums2.length % 2 == 1) res ^= xor1;
        if (nums1.length % 2 == 1) res ^= xor2;
        return res;
    }
}