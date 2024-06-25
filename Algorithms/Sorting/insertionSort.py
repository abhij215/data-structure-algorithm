"""Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list 
into its correct position in a sorted portion of the list. It is a stable sorting algorithm, meaning that elements 
with equal values maintain their relative order in the sorted output.

Space Complexity : O(1)
Time Complexity : O(N2)"""

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

"""
Advantages of Insertion Sort:
Simple and easy to implement.
Stable sorting algorithm.
Efficient for small lists and nearly sorted lists.
Space-efficient.

Disadvantages of Insertion Sort:
Inefficient for large lists.
Not as efficient as other sorting algorithms (e.g., merge sort, quick sort) for most cases.

Applications of Insertion Sort:
Insertion sort is commonly used in situations where:
The list is small or nearly sorted.
Simplicity and stability are important."""