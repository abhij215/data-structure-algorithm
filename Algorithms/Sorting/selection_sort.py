def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        start_element = i
        for j in range(i+1, n):
            if arr[start_element] > arr[j]:
                start_element = j
        arr[i], arr[start_element] = arr[start_element], arr[i]
    return arr

def selectionSortwhileloop(arr):
    n = len(arr)
    i = 0

    while i < n:
        min = i
        j = i+1
        while j < n:
            if arr[min] > arr[j]:
                min = j
            arr[min], arr[i] = arr[i], arr[min]
    return arr


if __name__ == "__main__":
    arr = [6,1,4,3,9,7]
    selectionSort(arr)
    print(arr)
