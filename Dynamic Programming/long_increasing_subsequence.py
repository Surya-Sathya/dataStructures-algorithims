def longest_increasing_subsequence(A):
    #Create memoized array 
    LIS = [1] * len(nums)

    #For each index in our array, we will find all elements that are smaller than i, A[j]
    for i in range(len(nums)):
        index_list = [x for x in range(i) if x < i and nums[x]<nums[i]]
        
        #Then we will find which one has the largest value in our memoized array
        if len(index_list) > 0:
            maximum_path = 0
            for index in index_list:
                if LIS[index] > maximum_path:
                    maximum_path = LIS[index]

            #The path will be from this max path element to our index, and we update our array
            LIS[i] = maximum_path + 1

        print(f"Index List{index_list}")
    
    return max(LIS)

nums = [10,9,2,5,3,7,101,18]
print(longest_increasing_subsequence(nums))
#NOTE - > This can actually be done in O(n*logn) time, it would be very difficult to figure out how though :)