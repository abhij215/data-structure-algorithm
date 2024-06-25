
def partition(arr, low, high):
    pivot = arr[low]
    start = low + 1
    end = high

    while True:

        while start <= end and arr[start] <= pivot:
            start += 1
        while start <= end and arr[end] >= pivot:
            end -= 1
        
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
        else:
            break
    
    arr[low], arr[end] = arr[end], arr[low]

    return end

def quickSort(arr, low, high):
    if low < high:
        pos = partition(arr, low, high)
        quickSort(arr, low, pos - 1)
        quickSort(arr, pos + 1, high)


def selectionSort(arr,n):

    for i in range(n):
        start_element = i
        for j in range(i+1, n):
            if arr[start_element] > arr[j]:
                start_element = j
            
        arr[i], arr[start_element] = arr[start_element], arr[i]


def insertionSort(arr,n):
    for i in range(1,n):
        start_element = arr[i]
        j = i-1
        while j >= 0 and start_element < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = start_element
    
    return arr

if __name__ == "__main__":
    
    arr = [5,14,58,4,79,22,14,56,48,45]

    print(arr)

    quickSort(arr, 0, len(arr)-1)

    print(arr)

    #print(insertionSort(arr, len(arr)))

    #selectionSort(arr, len(arr))
    #print(arr)