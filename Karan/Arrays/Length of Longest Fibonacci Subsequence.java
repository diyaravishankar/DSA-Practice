import java.util.HashSet;
import java.util.HashMap;
public class Solution {
    public int lenLongestFibSubseq(int[] arr) {
        HashSet<Integer> numSet = new HashSet<>();
        for (int num : arr) {
            numSet.add(num);
        }
        int n = arr.length;
        HashMap<String, Integer> dp = new HashMap<>();
        int longest = 0;
        for (int j = 1; j < n; j++) {
            for (int i = 0; i < j; i++) {
                int prev = arr[j] - arr[i];
                if (prev < arr[i] && numSet.contains(prev)) {
                    String key = prev + "," + arr[i];
                    dp.put(arr[i] + "," + arr[j], dp.getOrDefault(key, 2) + 1);
                    longest = Math.max(longest, dp.get(arr[i] + "," + arr[j]));
                }
            }
        }
        return longest >= 3 ? longest : 0;
    }
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] arr1 = {1, 2, 3, 4, 5, 6, 7, 8};
        System.out.println(solution.lenLongestFibSubseq(arr1));
        int[] arr2 = {1, 3, 7, 11, 12, 14, 18};
        System.out.println(solution.lenLongestFibSubseq(arr2));
    }
}