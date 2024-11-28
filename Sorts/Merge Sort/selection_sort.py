#Probably favour O(n^2) of Insertion Sort. Worst case they are both the same
#BUT when an element is in its actual position:
#1) Selection sort will still iterate through n-x of the rest of the array
#2) While insertion sort will simply move to the next element
#There is always a chance an element is in the right spot, hence insertion sort will be better in those cases

def selection_sort(A):
    for sorted_index, ele in enumerate(A):
        min = A[sorted_index]
        min_index = sorted_index
        print(f"Sorted_index:{sorted_index}")
        print(f"Min:{min}")

        for j in range(sorted_index + 1, len(A)):
            print(j)
            if A[j] < min:
                min = A[j]
                min_index = j
        
        print(f"Min:{min}")
        print(f"Min Index:{min_index}")
        
        A[sorted_index], A[min_index] = A[min_index], A[sorted_index]
        print(A)
    
    return A

A = [4, 3, 2, 1]
res = selection_sort(A)
print(res)
            
