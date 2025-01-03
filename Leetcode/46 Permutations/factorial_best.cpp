#include <vector>
#include <iostream>

using namespace std;

class Solution {
vector<vector<int>> res; 

private:
    void permute(int pos, int n, vector<int>& nums, vector<int> curr) {
        if(n == nums.size()-1) {
            res.push_back(curr);
            //cout << "---------" << endl; 
            return;
        }

        for(int i = n; i < nums.size(); i++) {
            //cout << "Swap pos n: " << n << ", with pos i: " << i << endl;
            vector<int> tmp_curr = curr;
            // int to_swap = tmp_curr[pos];
            // int swapping = tmp_curr[i];

            // tmp_curr[pos] = swapping;
            // tmp_curr[i] = to_swap; 

            swap(tmp_curr[pos], tmp_curr[i]); 

            permute(pos+1, n+1, nums, tmp_curr); 
        }
    }

public:
    vector<vector<int>> permute(vector<int>& nums) {
        permute(0, 0, nums, nums);

        return res; 
    }
};