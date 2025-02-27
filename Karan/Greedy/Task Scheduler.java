import java.util.*;
class Solution {
int leastInterval(char[] tasks, int n) {
int[] freq=new int[26];
for(char t:tasks) freq[t-'A']++;
Arrays.sort(freq);
int maxFreq=freq[25],idleSlots=(maxFreq-1)*(n+1),countMaxFreq=0;
for(int f:freq) if(f==maxFreq) countMaxFreq++;
return Math.max(tasks.length,idleSlots+countMaxFreq);
}
public static void main(String[] args) {
Solution sol=new Solution();
System.out.println(sol.leastInterval(new char[]{'A','A','A','B','B','B'},2));
System.out.println(sol.leastInterval(new char[]{'A','C','A','B','D','B'},1));
System.out.println(sol.leastInterval(new char[]{'A','A','A','B','B','B'},3));
}
}