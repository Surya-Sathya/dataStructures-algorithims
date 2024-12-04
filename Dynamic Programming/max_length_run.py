def longest_run(A):
    length = len(A) - 1
    i, j = 0,0
    runs = []

    while j < length:
        global count
        count += 1
        print(f"This is the #{count} call")
        if i == j:
            j += 1

        while A[j] > A[j-1] and j < length:
            j += 1
        
        print(f"i:{i}, j:{j}")

        # if j-i == 1:
        #     longest_run.append(j-i)
        # else:
        #     longest_run.append(j-i+1)
        
        runs.append((A[i], A[j-1]))

        i = j
    
    return runs

count = 0
Array = [2, 4, 3, 5, 1, 7, 6, 9, 8]
print(longest_run(Array))   
#Prints the longest run in an Array. A run is defined as a contiguous, increasing sequence. This is not a good implementation btw  