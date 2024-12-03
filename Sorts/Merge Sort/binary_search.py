def binary_search(A, l, h, target): 
    if h < l:
        return False

    mid = (l+h)//2
    print(f"mid:{mid}")

    if A[mid] == target:
        return True

    elif target < A[mid]:
        print(f"binary_search({A}, {l}, {mid-1}, {target})")
        return binary_search(A, l, mid-1, target)

    elif target > A[mid]:
        print(f"binary_search({A}, {mid+1}, {h}, {target})")
        return binary_search(A, mid+1, h, target)


A = [1, 5, 8, 9, 12, 14]
print(binary_search(A, 0, len(A)-1, 9))
