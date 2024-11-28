def insertion_sort(A: list):
    for count, ele in enumerate(A):
        j = count
        i = j -1
        if i != -1:
            while A[j] < A[i] and j != 0:
                A[j], A[i] = A[i], A[j]
                j -= 1
                i -= 1
                
    return A

A = [5, 1, 1, 1, 1]
res = insertion_sort(A)
print(res)

#check what : list does