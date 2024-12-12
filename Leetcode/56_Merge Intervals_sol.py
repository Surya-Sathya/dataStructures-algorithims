def merge_intervals(A):
    #Tim sort -> O(n*logn) combination of Merge/Insertion sort + O(n) space
    A.sort(key = lambda x:x[0])
    
    #O(n) space complexity max here if we don't merge any intervals
    res = [A[0]]

    #Linear traversal hence O(n) time here
    for start, end in A[1:]:
        res_start = res[-1][0]
        res_end = res[-1][1]

        if start <= res_end:
            res[-1] = [res_start, max(res_end, end)]
        
        elif start > res_end:
            res.append([start, end])
    
    return res

intervals = [[1,4], [0,4], [7,8], [3,3]]
print(merge_intervals(intervals))


