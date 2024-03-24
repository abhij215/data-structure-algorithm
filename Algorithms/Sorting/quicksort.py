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
