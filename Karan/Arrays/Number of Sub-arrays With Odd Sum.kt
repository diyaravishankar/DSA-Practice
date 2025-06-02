class Solution {
    fun numOfSubarrays(arr: IntArray): Int {
        val MOD = 1_000_000_007
        var evenCount = 1
        var oddCount = 0
        var prefixSum = 0
        var result = 0
        for (num in arr) {
            prefixSum += num
            if (prefixSum % 2 == 0) {
                result = (result + oddCount) % MOD
                evenCount++
            } else {
                result = (result + evenCount) % MOD
                oddCount++
            }
        }
        return result
    }
}