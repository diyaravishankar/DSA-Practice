import java.util.*;

class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<>();
        Map<String, Boolean> palindromeMemo = new HashMap<>();
        backtrack(s, 0, new ArrayList<>(), result, palindromeMemo);
        return result;
    }

    private void backtrack(String s, int start, List<String> path, List<List<String>> result, Map<String, Boolean> memo) {
        if (start == s.length()) {
            result.add(new ArrayList<>(path));
            return;
        }

        for (int end = start + 1; end <= s.length(); end++) {
            String substring = s.substring(start, end);
            if (isPalindrome(substring, memo)) {
                path.add(substring);
                backtrack(s, end, path, result, memo);
                path.remove(path.size() - 1);  // backtrack
            }
        }
    }

    private boolean isPalindrome(String str, Map<String, Boolean> memo) {
        if (memo.containsKey(str)) return memo.get(str);

        int left = 0, right = str.length() - 1;
        while (left < right) {
            if (str.charAt(left++) != str.charAt(right--)) {
                memo.put(str, false);
                return false;
            }
        }
        memo.put(str, true);
        return true;
    }
}
