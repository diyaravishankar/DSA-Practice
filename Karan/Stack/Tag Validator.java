public class Solution {
Stack<String> stack = new Stack<>();
boolean containsTag = false;
private boolean isValidTagName(String s, boolean ending) {
if (s.length() < 1 || s.length() > 9) return false;
for (char c : s.toCharArray()) {
if (!Character.isUpperCase(c)) return false;
}
if (ending) {
if (!stack.isEmpty() && stack.peek().equals(s)) stack.pop();
else return false;
} else {
stack.push(s);
containsTag = true;
}
return true;
}
public boolean isValid(String code) {
int i = 0, n = code.length();
if (n == 0 || code.charAt(0) != '<') return false;
while (i < n) {
if (i + 9 <= n && code.startsWith("<![CDATA[", i)) {
if (stack.isEmpty()) return false;
int j = code.indexOf("]]>", i + 9);
if (j < 0) return false;
i = j + 3;
} else if (code.startsWith("</", i)) {
int j = code.indexOf('>', i + 2);
if (j < 0) return false;
String tag = code.substring(i + 2, j);
if (!isValidTagName(tag, true)) return false;
i = j + 1;
if (stack.isEmpty() && i != n) return false;
} else if (code.charAt(i) == '<') {
int j = code.indexOf('>', i + 1);
if (j < 0) return false;
String tag = code.substring(i + 1, j);
if (!isValidTagName(tag, false)) return false;
i = j + 1;
} else {
if (stack.isEmpty()) return false;
i++;
}
}
return stack.isEmpty() && containsTag;
}
}