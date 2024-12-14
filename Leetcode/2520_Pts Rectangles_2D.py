def countRectangles(rectangles, points):
    res = []

    #initialise empty rectangle list of lists: h = 1 to h = 100, h is static
    rec_map = [[] for x in range(0, 101)]

    #fill rectangle list of lists: h = 1 to h = 100 with rectangles
    for rec_width, rec_length in rectangles:
        rec_map[rec_length].append(rec_width)

    #sort each sublist
    for length_bin in rec_map:
        length_bin.sort()

    def BinarySearch(A, l, r, key):       
        mid = (l+r)//2
        #print(f"Mid Calculation: {mid}")

        if r < l:
            if r == -1:
                return l
            return mid

        if A[mid] == key:
            return mid #return the mid, not the key

        if key > A[mid]: return BinarySearch(A, mid+1, r, key)
        if key < A[mid]: return BinarySearch(A, l, mid-1, key)
    

    #for each point[1] = x, we need to binary search the x height bin, and every binary search every bin after that as well 
    for pt_width, pt_length in points:
        rec_accum = 0
        print(f"Searching for point: {pt_width, pt_length} in rec_map[{pt_length}:101]")
        
        print(rec_map[pt_length:101], len(rec_map[pt_length:101]))
        for rec_length_bin in rec_map[pt_length:101]:
            if len(rec_length_bin) > 0: 
                idx = BinarySearch(rec_length_bin, 0, len(rec_length_bin)-1, pt_width)
                rec_accum += idx + 1
    
        res.append(rec_accum)

    return res


r = [[1,1],[2,2],[3,3]]
p = [[1,3],[1,1]]
print("Expected: [1, 3]")
print(f"Actual: {countRectangles(r, p)}")