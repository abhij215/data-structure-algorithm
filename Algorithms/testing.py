def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        min_indx = i
        for j in range(i+1,n):
            if arr[min_indx] > arr[j]:
                min_indx = j
        arr[min_indx], arr[i] = arr[i], arr[min_indx]
    
    return arr