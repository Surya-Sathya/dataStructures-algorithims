#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <utility>
#include <queue>

using namespace std; 
class Solution {
public:
    int maxScore(string s) {
        int score = 0; 
        
        for(int p = 1; p < s.size(); p++) {
            int temp = 0;

            for(int i = 0; i < p; i++) {
                if(s[i] == '0') temp++;
            }

            for(int j = p; j < s.size(); j++) {
                if(s[j] == '1') temp++; 
            }

            score = max(score, temp); 
        }

        return score; 
    }
};


