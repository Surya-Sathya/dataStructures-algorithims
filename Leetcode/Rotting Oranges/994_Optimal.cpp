#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <utility>
#include <queue>
using namespace std; 

//Multi-source BFS
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int mins = -1;  
        int fresh = 0; 
        vector<pair<int, int>> dir = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}}; 
        queue<pair<int, int>> q;
        int m = grid.size(); 
        int n = grid[0].size(); 

        for(int row = 0; row < m; row++) 
            for(int col = 0; col < n; col++) {
                if(grid[row][col] == 1) fresh++; 
                if(grid[row][col] == 2) q.push({row, col}); 
            }
        if(fresh == 0) return 0;


        while(!q.empty()) {
            int q_size = q.size(); 
            while(q_size--) {
                pair<int, int> cell = q.front();
                q.pop(); 

                for(pair<int, int> d : dir) {
                    int r = cell.first + d.first;
                    int c = cell.second + d.second;
                    if(r>=0 && c>=0 && r<m && c<n && grid[r][c] == 1) {
                        grid[r][c] = 2; 
                        fresh--; 
                        q.push({r, c}); 
                    }
                }
            }
            mins++; 
        }
        if(fresh == 0) return mins; 
        else return -1;
    }
};