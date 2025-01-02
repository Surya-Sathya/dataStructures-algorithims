#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <utility>
#include <queue>
using namespace std; 

class Solution1 {
public:
    int maxScore(string s) {
        int score= 0;
        int ones = 0; 
        int zeroes = 0;

        for(char c : s) {
            if(c == '1') ones++; 
        }

        for(int i = 0; i < s.size()-1; i++) {
            if(s.at(i) == '0') zeroes++; //adding 0 to left substring
            else ones--; //removing a one from right substring 

            score = max(score, zeroes + ones);
        }

        return score; 
    }
};

class Solution2 {
public:
    /*Based on: Score = 0's Left + 1's Right
                Score = 0's Left + 1's Total - 1's Left
                Score = (0's Left - 1's Left) + 1's Total
    The only that that dynamically changes is the 0l and 1l sizes, hence iterate and maximise this value
    */
    int maxScore(string s) {
        int zeroes= 0;
        int ones = 0; 
        int t_ones = 0; 
        int zeroMinusone_left = INT_MIN;

        for(int i = 0; i < s.size()-1; i++) {
            char c = s[i];

            if(c == '1') {
                t_ones++;
                ones++; 
            }
            else zeroes++;
            //cout << "Num of Zeroes: " << zeroes << " , Number of Ones: " << ones << " , when L ends: " << i << endl;

            zeroMinusone_left = max(zeroes - ones, zeroMinusone_left);
        } 

        if(s.back() == '0') return zeroMinusone_left + t_ones; 
        else return zeroMinusone_left + t_ones + 1; 
    }
};