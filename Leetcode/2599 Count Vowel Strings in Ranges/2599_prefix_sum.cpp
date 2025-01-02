#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <utility>
#include <queue>
using namespace std; 

//DON"T USE STOI/TOSTRING, increase complexity + unordered set
class Solution {
public:
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        unordered_set<char> v = {'a', 'e', 'i', 'o', 'u'}; 
        vector<int> p_sum(words.size()); 
        int valid = 0;

        for(int i = 0; i < words.size(); i++) {
            char fr = words[i].front();
            char ba = words[i].back();
            p_sum[i] = valid;  

            if(v.contains(fr) && v.contains(ba)) p_sum[i] = ++valid;
        }

        vector<int> res;
        for(vector<int> q : queries) {
            int q0 = q[0]-1;
            int q1 = q[1];
            
            (q0 == -1 ? res.push_back(p_sum[q1]) : res.push_back(p_sum[q1] - p_sum[q0])); 
        }

        return res;
    }
};