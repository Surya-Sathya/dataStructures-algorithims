#include <vector>
#include <iostream>
using namespace std; 

class Solution {
public:
    int climbStairs(int n) {
        // int res = 0;
        // res = 1 + combinate(n-1, 1); 
        // return res; 

        // if(n==1) return 1;   
        // int res = 1;
        // int N = n-1; 

        // for(int r = 1; r <= N; r++) {
        //     cout << N << " " << r << " " << fact(N)/(fact(r) * fact(N-r)) << "\n";  
        //     res += fact(N)/(fact(r) * fact(N-r));
        //     N--; 
        // }
        // return res;  

        //Backtracking approach: Too much time complexity
        int res = 0; 
        dfs(0, n, res);
        return res;
    }

    void dfs(int running_sum, int target, int& res) {
        if(running_sum == target) {
            res += 1; 
            cout << "Sum " << running_sum <<" found" << "\n"; 
            return; 
        } else if(running_sum > target) {
            return;
        }

        cout << "Running Sums: " << running_sum << " "; 
        cout << running_sum + 1 << " " << running_sum +2 << " " << "\n"; 
        //cout << "Running Sum: " << running_sum << "\n"; 
        dfs(running_sum + 1, target, res);
        dfs(running_sum + 2, target, res);
        return; 
    }

    int fact(int a) {
        if(a==1 || a==0) return 1;

        int ans = 1; 
        for(int i = 2; i<=a; i++) ans *= i; 
        return ans; 
    }

    int combinate(int n, int r) {
        if(n==r) return 1;
        if(n<r) return 0;

        return (fact(n)/(fact(r) * fact(n-r))) + combinate(n-1, r+1);
    }

};


    int climbStairs(int n) {
        //Fibonacci Sequence:
        if(n == 0) return 0; 
        if(n == 1) return 1; 
        //Store in O(n) vector to prevent stack overflow -> tabulation, dyanmic bottom up
        //Memoization actually uses recursion, and has call stack, but stores fib(4) in hashmap

        int n_minus1 = 1;
        int n_minus2 = 1; 
        int curr = 0;

        for(int i = 2; i <= n; i++){
            curr = n_minus1 + n_minus2;
            n_minus2 = n_minus1;
            n_minus1 = curr;
        }

        return curr;
    }