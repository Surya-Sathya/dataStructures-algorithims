def countRectangles(rectangles, points):
    rectangles.sort() #[1, 3, 4, 5]
    res = []

    #Find the first index which's rectangle is larger than the 1D point

    def BinarySearch(A, l, r, key):       
        mid = (l+r)//2
        print(f"Mid Calculation: {mid}")

        if r < l:
            print("Not found, return index where it should be inserted")
            return mid

        if A[mid] == key:
            return mid #return the mid, not the key

        if key > A[mid]: return BinarySearch(A, mid+1, r, key)
        if key < A[mid]: return BinarySearch(A, l, mid-1, key)
    
    for point in points:
        print(f"Searching for point: {point} in array: {rectangles}")
        idx = BinarySearch(rectangles, 0, len(rectangles)-1, point)
        res.append(idx+1)
    
    return res


r = [5, 4, 1, 3]
p = [2, 4, 9]
print("Expected: [1, 3, 4]")
print(f"Actual: {countRectangles(r, p)}")