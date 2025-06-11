class Solution {
    public int minimizeXor(int num1, int num2) {
        int count = Integer.bitCount(num2);
        int x = 0;
        for (int i = 31; i >= 0 && count > 0; i--) {
            if (((num1 >> i) & 1) == 1) {
                x |= (1 << i);
                count--;
            }
        }
        for (int i = 0; i <= 31 && count > 0; i++) {
            if (((x >> i) & 1) == 0) {
                x |= (1 << i);
                count--;
            }
        }
        return x;
    }
}