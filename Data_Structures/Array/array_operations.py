# 01_function for linear searching of elements in an array
def linearSearch(arr, ln, findElement):
    for i in range(ln):
        if arr[i] == findElement:
            return i
    else:
        return -1

# 02_function for binary searching of elements in an sorted array
def binarySearch(arr, low, high, target):
    if high>=1:         
         mid = low + (high-low)//2
         if arr[mid] == target:
            return mid
         elif arr[mid] > target:
            return binarySearch(arr, low, mid-1, target)
         else:
            return binarySearch(arr, mid+1, high, target)
         
    else:
        return -1
    

def whileBinarySearch(arr, low, high, target):
    while low <= high:
        mid = (low+high)//2

        if arr[mid] > target:
            high = mid-1
        elif arr[mid] < target:
            low = mid+1
            


# 03_function to reverse an array
def reverseUsingRecurrsion(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverseUsingRecurrsion(arr, start+1, end-1)

# 04_function to rotate an array
#def rotater(arr, rotate):


#Driver function
if __name__ == "__main__":
    arr = [10,11,12,13,14,15,16,17,18,19,20,21]
    ln = len(arr)
    findElement = 20
    rotate = 2
    
    #linear search method
    linearIndex = linearSearch(arr, ln, findElement)

    if linearIndex == -1:
        print("no such element found")
    else:
        print(linearIndex)

    # Binary Search Method
    BinarySearchIndex = binarySearch(arr, 0, ln-1, findElement)

    if BinarySearchIndex == -1:
        print('no element is found')
    else:
        print(BinarySearchIndex)

    # reversing an Array
    print('before reversing'+ str(arr))
    reverseUsingRecurrsion(arr, 0, ln-1)
    print("after reversing")
    print(arr)

    # rotate an Array
    #rotater(arr,)