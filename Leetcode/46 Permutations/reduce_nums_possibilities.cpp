#include <vector>
using namespace std; 

class Solution {
vector<vector<int>> res; 

private:
    void dfs(vector<int> nums, vector<int> curr) {
        if(nums.empty()) {
            res.push_back(curr);
            return;
        }

        for(int i = 0; i < nums.size(); i++) {
            vector<int> tmp_curr = curr;
            tmp_curr.push_back(nums[i]);

            vector<int> tmp_nums = nums;
            tmp_nums.erase(tmp_nums.begin()+i);

            dfs(tmp_nums, tmp_curr); 
        }
    }

public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> curr;
        dfs(nums, curr);

        return res; 
    }
};