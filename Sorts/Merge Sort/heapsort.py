def heapsort(A):
    #1 Create heap (left to right, i.e. not heapify)
    for index, node in enumerate(A):
        if index % 2 == 0: parent_index = index//2
        else: parent_index = (index - 1)//2

        while A[parent_index] < A[index]:
            A[parent_index], A[index] = A[index], A[parent_index]
            index = parent_index
            if parent_index % 2 == 0: parent_index = index//2
            else: parent_index = (parent_index - 1)//2  

    print(A)
    #2 Switch last node and first node, push last node down
    for index, node in enumerate(A):
        end = len(A)-1-index
        A[0], A[end] = A[end], A[0]
        print(f"After initial swap: {A}")

        leftChild = 1
        rightChild = 2

        print(f"Index {index}: lc:{leftChild}, rc:{rightChild}, end = {end}")

        while leftChild < end and rightChild < end:
            #Find biggest of two children
            if leftChild < end and rightChild < end:
                if A[leftChild] > A[rightChild]: maxIndex = leftChild
                elif A[rightChild] > A[leftChild]: maxIndex = rightChild
                elif A[rightChild] == A[leftChild]: maxIndex = leftChild
            
            if leftChild >= end and rightChild < end: maxIndex = rightChild
            if leftChild < end and rightChild >= end: maxIndex = leftChild
            
            print(f"Index {index}: lc:{leftChild}, rc:{rightChild}")
            print(f"Max Index: {maxIndex}")
            if A[maxIndex] > A[i]:
                A[maxIndex], A[i] = A[i], A[maxIndex]
            i = maxIndex

            leftChild = i*2
            rightChild= i*2 + 1
            print(f"Child Swap: {A}")
            
    return A
            
        #A[0], A[-1] = A[-1], A[0]
Array = [15, 20, 10, 40, 30]
print(heapsort(Array))