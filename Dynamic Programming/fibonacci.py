i = 0

def fib(n):
    global i  # Declare that 'i' is a global variable
    i = i + 1
    print(f"This is call #{i}")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fib_dp(n):
    #Dynamic programming using memoization for linear time and linear space 
    dp = [None] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n], dp

#BUDS:
#   Bottlenecks
#   Unnecessary Work 
#   Duplicated Work

print(fib_dp(6))
