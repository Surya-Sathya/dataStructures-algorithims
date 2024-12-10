def power(a,n):
    if n == 0:
        return 1
    
    if n % 2 == 0:
        print(f"One squaring (^2) operator for (power({a}, {n}/2))**2")
        return (power(a, n/2))**2
    
    elif n % 2 == 1:
        print(f"One squaring (^2) operator and One Multiply Operator for {a}*(power({a}, {n}/2))**2")
        return a*(power(a, n//2))**2

a = 2
n = 11
print(power(a, n))
print(f"This would have been done in {n-1} multiply operators otherwise -> O(n) compard to Log(n) in recursive form")

#For 2^11, we get 4 print statements (4 recursive calls). Each print statement at worst represents two multiplications (for when x is odd)
#The amount of recursive calls we get is how many times we can split 11 into halves, or log2(11) ~ 3.459 = 4 calls
#Hence Hence the amount of time steps to mulitply t(n) = 2*log(n) + (C)*log(n) (C = amount of O(1) steps in if statements/assignments per call)
# O(2Clog(n)) -> O(log(n)), as there exists some c that bounds this t(n). Also a c2 which lower bounds it; hence O-sigma = O(logn)

#Recursive formula => a^(n) = (a^(n/2))*2