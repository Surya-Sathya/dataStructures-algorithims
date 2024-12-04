def maxSubArray(A):
    dp = [None] * len(A)
    max_subarray = float("-inf")

    for index, element in enumerate(A):
        if index == 0:
            dp[0] = element
        
        else:
            dp[index] = max(element, dp[index - 1] + element)

    for ele in dp:
        if ele > max_subarray:
            max_subarray = ele
    
    return max_subarray, dp

Array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(Array))
#This function returns the length of the maximum sum, contiguous subarray in Array
#This can actually be done in O(1) space, but would take too long to implement right now, a bit too finicky
               