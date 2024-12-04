def quadratic_max(A):
    ans = float("-inf")
    
    for i in range(len(A)):
        local_sum = 0

        for j in range(i, len(A)):
            local_sum += A[j]
            ans = max(ans, local_sum)
    
    return ans

def non_contiguous_max(A, i):
    if i == 0: 
        return A[0]

    return max(non_contiguous_max(A, i-1), non_contiguous_max(A, i-1) + A[i])

ans = float("-inf")
Array = [1, -10, 1, -20, -40, 1]
print(quadratic_max(Array))
print(non_contiguous_max(Array, len(Array) - 1))
