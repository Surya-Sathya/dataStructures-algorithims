#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>  // To measure time

std::vector<int> candidates = {1, 5, 8, 9, 10, 17, 17, 20, 24, 30};
std::vector<int> dp;

int max_value_at_len(int len) {
    if(len <= 0) return 0; 
    if(dp[len] != -1) return dp[len];

    int curr_max = 0;
    for(int i = 0; i < len+1; i++) {  // Iterating up to len+1
        if(len-i-1 >= 0) curr_max = std::max(curr_max, candidates[i] + max_value_at_len(len-i-1));
    }
    dp[len] = curr_max; 
    return curr_max;
}

int max_value_at_candidates(int len) {
    if(len <= 0) return 0; 
    if(dp[len] != -1) return dp[len];

    int curr_max = 0;
    for(int i = 0; i < candidates.size(); i++) {  // Iterating over candidates size
        if(len - i - 1 >= 0) curr_max = std::max(curr_max, candidates[i] + max_value_at_candidates(len - i - 1));
    }
    dp[len] = curr_max;
    return curr_max;
}

int main() {
    int L = 40;
    int temp = L + 1;
    while (temp--) dp.push_back(-1);

    // Run the test multiple times for better time measurement
    int num_runs = 100;

    // Time measurement for using len+1
    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < num_runs; ++i) {
        max_value_at_len(L);  // Run the function multiple times
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto duration_len = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    std::cout << "Time taken with len+1 (after " << num_runs << " runs): " << duration_len.count() << " ms\n";

    // Reset dp array for the next function call
    dp.clear();
    temp = L + 1;
    while (temp--) dp.push_back(-1);

    // Time measurement for using candidates.size()
    start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < num_runs; ++i) {
        max_value_at_candidates(L);  // Run the function multiple times
    }
    end = std::chrono::high_resolution_clock::now();
    auto duration_candidates = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    std::cout << "Time taken with candidates.size() (after " << num_runs << " runs): " << duration_candidates.count() << " ms\n";

    return 0;
}
