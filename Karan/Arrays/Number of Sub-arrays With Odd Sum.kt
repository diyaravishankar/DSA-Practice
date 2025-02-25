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
fun main() {
    println(numOfSubarrays(intArrayOf(1,3,5))) 
    println(numOfSubarrays(intArrayOf(2,4,6))) 
    println(numOfSubarrays(intArrayOf(1,2,3,4,5,6,7)))  
}