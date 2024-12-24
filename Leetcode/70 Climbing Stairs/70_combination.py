import math as m

class Solution:
    def climbStairs(self, n: int) -> int:
        res = 1
        N = n-1
        
        for r in range(1, n):
            if r > N: return res

            res += m.comb(N, r)
            N -= 1
        
        return res