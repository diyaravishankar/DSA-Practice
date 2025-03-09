#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 int minGroups(vector<vector<int>>& intervals) {
  vector<pair<int, int>> events;
  for (auto& it : intervals) {
   events.push_back({it[0], 1});
   events.push_back({it[1] + 1, -1});
  }
  sort(events.begin(), events.end());
  int maxGroups = 0, active = 0;
  for (auto& e : events) {
   active += e.second;
   maxGroups = max(maxGroups, active);
  }
  return maxGroups;
 }
};