def Partition(l, h):
    pivot = l
    i = l + 1
    j = h

    while j > i:
        while A[i] < A[pivot]:
            i += 1
            print(f"i: {i}")
        while A[j] > A[pivot]:
            j -= 1
            print(f"j: {j}")

        if j > i:        
            print(f"Before Swap: {A}")
            A[i], A[j] = A[j], A[i]
            print(f"After Swap {A}")

    A[pivot], A[j] = A[j], A[pivot]
    print(A)
    return j

# def Quicksort(l, h):
#     if l < h: 
#         j = Partition(l, h)
#         Quicksort(l, j)
#         Quicksort(j+1, h)

def Quicksort_array(A):
    A.append(float('inf'))
    l = 0
    h = len(A) - 1

    j = Partition(l, h)
    Partition(l, j)
    Partition(j+1, h)

A = [3, 4, 2, 1]
Quicksort_array(A)
print(f"Final Sorted Array: {A}")

