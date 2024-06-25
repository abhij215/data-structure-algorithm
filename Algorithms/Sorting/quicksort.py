"""QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot and 
partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

Time Complexity: O(N2)
Space Complexity: O(1)"""

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
   
    

def quicksort(arr, low, high):
   if low < high:
      pos = partition(arr, low, high)
      quicksort(arr, low, pos-1)
      quicksort(arr, pos+1, high)
   


if __name__ == "__main__":
   arr = [5, 1, 8, 3, 2]
   quicksort(arr, 0, len(arr)-1)
   print(arr)


"""Advantages of Quick Sort:
It is a divide-and-conquer algorithm that makes it easier to solve problems.
It is efficient on large data sets.
It has a low overhead, as it only requires a small amount of memory to function.

Disadvantages of Quick Sort:
It has a worst-case time complexity of O(N2), which occurs when the pivot is chosen poorly.
It is not a good choice for small data sets.
It is not a stable sort, meaning that if two elements have the same key, their relative order 
will not be preserved in the sorted output in case of quick sort, because here we are swapping 
elements according to the pivot’s position (without considering their original positions)."""
