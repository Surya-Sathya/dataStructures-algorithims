#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <utility>
#include <queue>
using namespace std; 

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        vector<pair<int, int>> dir = {{0, -1}, {0, 1}, {1, 0}, {-1, 0}};
        int m = grid.size();
        int n = grid[0].size();

        vector<pair<int, int>> island_tiles; 
        for(int r = 0; r < m; r++)
            for(int c = 0; c < n; c++) 
                if(grid[r][c] == '1') island_tiles.push_back({r, c}); 
    
        queue<pair<int, int>> q;
        int num_islands = 0;
        for (pair<int, int> island : island_tiles)
            if(grid[island.first][island.second] == '1') {
                num_islands++; 
                q.push({island.first, island.second}); 

                while(!q.empty()) {
                    pair<int, int> visiting = q.front();
                    q.pop();
                    grid[visiting.first][visiting.second] = 0; 

                    for(pair<int, int> direction : dir) {
                        int r_adj = visiting.first + direction.first;
                        int c_adj = visiting.second + direction.second;

                        if(r_adj >= 0 && c_adj >= 0 && r_adj < m && c_adj < n && grid[r_adj][c_adj] == '1') {
                            grid[r_adj][c_adj] = 0;
                            q.push({r_adj, c_adj}); 
                        }
                    }
                }
            }

        return num_islands; 
    }
};