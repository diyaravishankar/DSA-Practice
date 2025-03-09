#include <bits/stdc++.h>
using namespace std;
class Solution { 
public:
 int smallestChair(vector<vector<int>>& times, int tgt) { 
  int n = times.size();vector<pair<int, int>> arr;
  for (int i = 0; i < n; i++) arr.push_back({times[i][0], i});
  sort(arr.begin(), arr.end());
  priority_queue<int, vector<int>, greater<int>> freeChairs;
  priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> occ;
  int chairCnt = 0;
  for (auto& [t, idx] : arr) { 
   while (!occ.empty() && occ.top().first <= t) { 
    freeChairs.push(occ.top().second);occ.pop();
   }
   int chair = freeChairs.empty() ? chairCnt++ : freeChairs.top();
   if (!freeChairs.empty()) freeChairs.pop();
   occ.push({times[idx][1], chair});
   if (idx == tgt) return chair;
  }
  return -1;
 }
};