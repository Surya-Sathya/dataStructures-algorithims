def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    res = []
    l = 0
    r = len(intervals) - 1

    def merge_sort(Array,l,r):
        if l == r: return

        mid = (l+r)//2
        print(f"mid: {mid}, l: {l}, r: {r}")
        merge_sort(Array, l, mid)
        merge_sort(Array, mid+1, r)
        print(f"l: {l}, r: {r}")
        combine(l, r)

    def combine(l, r):
        minL = intervals[l][0]
        maxL = intervals[l][1]
        minR = intervals[r][0]
        maxR = intervals[r][1]

        #one if just way more huge than the other
        if minL <= minR and maxL >= maxR:
            res.append([minL, maxL])

        elif minR <= minL and maxR >= maxL:
            res.append([minR, maxR])

        # 1 < 2, and 3 > 2
        elif minL <= minR and maxL >= minR:
            res.append([minL, maxR])

        elif minR <= minL and maxR <= minL:
            res.append([minR, maxL])

        elif minL >= minR and maxL <= maxR:
            res.append([minR, maxR])

        elif minR >= minL and maxR <= maxL:
            res.append([minL, maxL])

        elif maxL < minR:
            res.append(intervals[l])
            res.append(intervals[r])

        print(f"Combined {intervals[l]} with {intervals[r]} --> {res}")
        
    
    merge_sort(intervals, l, r)



#merge([[1,3],[2,6],[8,10],[15,18]])  
  




        
            