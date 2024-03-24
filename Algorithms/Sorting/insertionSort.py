

def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]

        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    

if __name__ == "__main__":
    arr = [6,1,4,3,9,7,5]
    insertionSort(arr)
    print(arr)
