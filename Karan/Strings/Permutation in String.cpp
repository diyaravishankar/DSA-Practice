#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.length() > s2.length()) return false;
        vector<int> freq1(26, 0), freq2(26, 0);
        for (char c : s1) freq1[c - 'a']++;
        for (int i = 0; i < s1.length(); i++) freq2[s2[i] - 'a']++;
        if (freq1 == freq2) return true;
        for (int i = s1.length(); i < s2.length(); i++) {
            freq2[s2[i] - 'a']++;
            freq2[s2[i - s1.length()] - 'a']--;
            if (freq1 == freq2) return true;
        }
        return false;
    }
};
void run() {
    Solution solution;
    cout << solution.checkInclusion("ab", "eidbaooo") << endl;
    cout << solution.checkInclusion("ab", "eidboaoo") << endl;
}