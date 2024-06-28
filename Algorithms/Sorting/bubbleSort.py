"""Bubble Sort, a basic sorting algorithm, operates by repeatedly swapping adjacent elements if they are incorrectly ordered.

Time Complexity: O(N2)
Space Complexity: O(1)"""

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        checker = 0
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                checker += 1
        if checker == 0:
            break


if __name__ == "__main__":
    arr = [6,1,1,4,3,9,7,5]
    bubbleSort(arr)
    print(arr)