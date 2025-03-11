#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <utility>
#include <queue>
#include <algorithm>

std::vector<int> candidates = {1, 5, 8, 9, 10, 17, 17, 20, 24, 30};
std::vector<int> dp; 

int max_value_at(int len) {
    //std:: cout << "Find max value at position: " << len << std::endl;

    if(len <= 0) return 0; 
    if(dp[len] != -1) {
        //std::cout << "Cached is at: " << len << " with a value of: " << dp[len] << std::endl;
        return dp[len];
    } 
    int curr_max = 0;

    //Complexity = #Sub problems * Non-recursive work at each subproblem => L+1 subprobs including BC => Theta(L) * O(L)
    for(int i = 0; i < len+1; i++) {
        if(len-i-1 >= 0) curr_max = std::max(curr_max, candidates[i] + max_value_at(len-i-1));
    }

    dp[len] = curr_max; 
    return curr_max; 
}

int main () {
    int L = 40;
    int temp = L+1;
    while(temp--) dp.push_back(-1); 

    std::cout << "Max Value: " << max_value_at(L); 
    return 0;
}