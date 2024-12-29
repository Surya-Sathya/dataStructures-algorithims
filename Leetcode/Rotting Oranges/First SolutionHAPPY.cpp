#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <pair>
using namespace std; 

/*
3 options for a grid -> 0 is empty, 1 fresh, 2 rotten
Every minute -> 4-directionally from 2 becomes 2 (only 1's not emptys)
If impossible (i.e. if there is a one that has an empty 4-directionally) -> add check later

*ALL Bfs searches have an o(v+e) complexity, and as you have to explore all edges all the time, 
    maybe it doesn't matter where you choose to start the ornage
*Think of contradictory step, doesn't matter where you start BFS from
-> MINIMUM number of minutes that has to elapse until all cells are either 2 or 0
    -> this means the starting orange matters???

1) Iterate through mxn and count number of fresh oranges
    1a) If fresh = 0, return 0
2) Iterate through mxn to find FIRST 2 rotten orange
    2a) If can't find rotten orange, return -1 (atp >= 1 fresh, hence no rotten means impossible)
3) Perform BFS with a queue
    3a) Hmm, counting is a problem, we will code BFS, and implementation dependent, we will see
    where to insert the counting, shouldn't be too hard
4) If total number of oranges after BFS has stopped, compare orange coun
    4a) If 0, then return **
    4b) If not 0, return -1 as there are some oranges left untouched
*/

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int mins = -1;  
        
        //Count fresh oranges and find rotten
        int fresh = 0; 
        vector<pair<int, int>> rottens;  
        int row_size = grid[0].size(); 

        for(int row = 0; row < grid.size(); row++) { 
            for(int col = 0; col < row_size; col++) {
                if(grid[row][col] == 1) fresh++; 
                if(grid[row][col] == 2) rottens.push_back(make_pair(row, col)); 
            }
        }
        //cout << fresh << endl;
        if(fresh == 0) return 0;
        //cout << "Rotten First: " << rotten.first << " " << rotten.second << endl;

        //Queue BFS and count ~ visited actually counts as "visited" grid
        //Pop back queue until completely empty
        queue<pair<int, int>> q;
        for(auto r : rottens) q.push(r); 
        while(!q.empty()) {

            //cout << "Level: " << mins << "----------------" << endl; 
            int q_size = q.size();  
            for(int i = 0; i < q_size; i++) {
                //cout << "First pop: " << q.front().first << " " << q.front().second << endl;
                pair<int, int> cell = q.front();
                q.pop(); 
                
                vector<pair<int, int>> neighbours = find_neighbours(grid, cell);
                for(pair<int, int> n : neighbours) {
                    if(grid[n.first][n.second] != 2) {
                        grid[n.first][n.second] = 2; 
                        fresh--; 
                        q.push(n); 
                    }
                }
            }
            mins++; 
        }
        if(fresh == 0) return mins; 
        else return -1;
    }

    vector<pair<int, int>> find_neighbours(vector<vector<int>>& grid, pair<int, int> cell) {
        vector<pair<int, int>> neighbours;
        int row = cell.first;
        int col = cell.second;
        //cout << "Search for neighbours of cell: " << row << ", " << col << endl;

        if(row - 1 > -1 && grid[row-1][col] == 1) neighbours.push_back(make_pair(row-1, col));
        if(col - 1 > -1 && grid[row][col-1] == 1) neighbours.push_back(make_pair(row, col-1));
        if(row + 1 < grid.size() && grid[row+1][col] == 1) neighbours.push_back(make_pair(row+1, col));
        if(col + 1 < grid[0].size() && grid[row][col+1] == 1) neighbours.push_back(make_pair(row, col+1));
        //for(auto n : neighbours) cout << n.first << " " << n.second << endl; 
        return neighbours; 
    }
};