#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
using namespace std; 

class Solution {
public:
    int scoreOfParentheses(string s) {
        //Input: Balanced parenthesis s -> always balanced, 
        //Output: Score of a string

        //You are given a BALANCED parenthesis (), ()(), (()); find the
        //Length is <50; edge case of 2 must be covered, 50 ~ weird, maybe not so fast algorithim?

        //Will always start with a '('

        int score = 0;
        vector<pair<int, int>> groups; 
        vector<int> visited(s.size(), 0); 

        for(int i = 0; i < s.size(); i+= 2) {
            cout << i << "\n"; 
            if(visited[i]) continue;
            else if(s[i] == '(' && s[i+1] == ')') score += 1;
            else {
                visited[i] =  1; 
                int count = 1;
                
                for(int r = i+1; r<s.size(); r++) {
                    cout << "r: " << r << "\n"; 
                    visited[r] = 1; 
                    if(s[r] == '(') ++count; 
                    else if(--count == 0) {
                        groups.push_back(make_pair(i, r)); 
                        break;
                    } 
                }
            }
        }

        for(auto& vec_pair : groups) {
            cout << vec_pair.first << " " << vec_pair.second << "\n"; 
            score += calc_score(vec_pair.first, vec_pair.second, s); 
        }

        return score; 
    }

    int calc_score(int start, int end, string s) {
        char st = s[start];
        char ed = s[end];

        //cout << "Actual: "<< start << " " << end << "\n"; 
        //(A)
        if(st == '(' && ed == ')' && start + 1 == end) return 1; 

        else if(st == '(' && ed == ')') {
            //cout << start + 1 << " " << end - 1 << "\n"; 
            return 2*calc_score(start+1, end-1, s); 
        } 

        //()
        else return (1/2) * (2 + calc_score(start+1, end-1, s));
    }
};


class Solution_O_One_space {
public:
    int scoreOfParentheses(string s) {
        
        int score = 0;
        int depth = 0;

        for(int i = 0; i < s.size(); i++) {

            if(s[i] == '(') ++depth;
            else --depth;

            if(s[i] == ')' && s[i-1] == '(') score += pow(2, depth);  
        }
        return score; 
    }
};


class Solution_stack {
public:
    int scoreOfParentheses(string s) {
        
        //current, as a VARIABLE holds the running tally of internal score
        //if we encounter ( after our current, then push the current and add it later
        int running_internal = 0;
        stack<int> st;

        for(char p : s) {

            if(p == '(') {
                st.push(running_internal);
                running_internal = 0; 
            } else {
                running_internal = running_internal + st.top() + max(1, running_internal);
                st.pop();
            }
        }

        return running_internal; 
    }
};