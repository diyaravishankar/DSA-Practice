#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        sort(skill.begin(), skill.end());
        int n = skill.size(), teamSkill = skill[0] + skill[n - 1];
        long long totalChemistry = 0;
        for (int i = 0, j = n - 1; i < j; i++, j--) {
            if (skill[i] + skill[j] != teamSkill) return -1;
            totalChemistry += (long long)skill[i] * skill[j];
        }
        return totalChemistry;
    }
};

void run() {
    vector<int> skill1 = {3,2,5,1,3,4}, skill2 = {3,4}, skill3 = {1,1,2,3};
    cout << Solution().dividePlayers(skill1) << endl;
    cout << Solution().dividePlayers(skill2) << endl;
    cout << Solution().dividePlayers(skill3) << endl;
}