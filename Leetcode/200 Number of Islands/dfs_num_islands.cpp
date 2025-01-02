#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <utility>
#include <queue>
using namespace std; 

class Solution {
private:
    void dfs(int r, int c, vector<vector<char>>& grid) {
        grid[r][c] = '#';
        int m = grid.size();
        int n = grid[0].size();

        if(r-1 >= 0 && grid[r-1][c] == '1') dfs(r-1, c, grid); 
        if(r+1 < m && grid[r+1][c] == '1') dfs(r+1, c, grid); 
        if(c-1 >= 0 && grid[r][c-1] == '1') dfs(r, c-1, grid); 
        if(c+1 < n && grid[r][c+1] == '1') dfs(r, c+1, grid); 

        return; 
    }

public:
    int num_islands = 0;

    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        //Find all locations of island cells
        for(int r = 0; r < m; r++) {
            for(int c = 0; c < n; c++) {
                if(grid[r][c] == '1') {
                    num_islands++;
                    dfs(r, c, grid);
                } 
            }
        }
        return num_islands;
    }
};