#linear Search
def linearSearch(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
#---------------------------------------------------------------------------------------

#binary Search
def binarySearch(arr, target):
    l,r = 0, len(arr)
    target = -1

    while l <= r:
        mid = (l+r)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
        
    return target
#---------------------------------------------------------------------------------------

#Binary Search
#Lower Bound
def lowerBound(arr,x):
    i,j = 0,len(arr)-1
    ans = 0

    while i <= j:
        mid = (i+j)//2

        if arr[mid] >= x:
            ans = mid
            i = mid -1
        else:
            j = mid + 1
        
    return ans
#---------------------------------------------------------------------------------------

#Binary Search
#Upper Bound
def upperBound(arr,x):
    i,j = 0,len(arr)-1
    ans = 0

    while i<=j:
        mid = (i+j)//2

        if arr[mid] <= x:
            ans = mid
            i = mid+1
        else:
            j = mid-1
        
    return ans
#---------------------------------------------------------------------------------------

#Binary Search
#Search Insert Position
def searchInsertPosition(arr,target):
    l,r = 0, len(arr)-1

    while l <= r:
        mid = (l+r)//2

        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] == target and arr[mid-1] != target:
            return mid
        else:
            r = mid - 1
    
    return l
#---------------------------------------------------------------------------------------

#Binary Search
#Find first and last occurance of element in sorted array
def firstAndLastOccurance(arr,target):
    l,r = 0, len(arr)-1

    while l <= r:
        if arr[l] == target and arr[r] == target:
            return [l,r]
        elif arr[l] < target:
            l += 1
        else:
            r -= 1
        
    return [-1.-1]

#---------------------------------------------------------------------------------------

#Count Occurrences in Sorted Array
def countOccurances(arr,target):
    cnt = 0

    for i in range(len(arr)):
        if arr[i] == target:
            cnt += 1
        
    return cnt

#---------------------------------------------------------------------------------------

#Binary Search
#Search in Rotate Sorted Array
def searchInRotatedSortedArray(arr, target):
    l,r = 0, len(arr)-1

    while l <= r:
        mid = (l+r)//2

        if arr[mid] == target:
            return mid
        
        if arr[l] < arr[mid]:
            if arr[l] < target and target < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
            
        else:
            if arr[mid] < target and target < arr[r]:
                l = mid + 1
            else:
                r = mid -1

#---------------------------------------------------------------------------------------

#Binary Search
#Find Minimum in Rotate Sorted Array
def minimumInRotatedSortedArray(arr):
    l,r = 0, len(arr)-1

    while l < r:

        mid = (l+r)//2

        if arr[mid] > arr[r]:
            l = mid + 1
        else:
            r = mid
        
    return l

#---------------------------------------------------------------------------------------

#Binary Search
#Find the Peak Element
def peakElement(arr):
    n = len(arr)

    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n-1] > arr[n-2]:
        return n-1
    
    l,r = 1, n-2

    while l <= r:
        mid = (l+r)//2

        if arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
            return mid
        elif arr[mid] > arr[mid-1]:
            l = mid + 1
        else:
            r = mid - 1

    return -1

#---------------------------------------------------------------------------------------

# 02 - peak element in a rotated sorted array
def findPeakElement(arr):
    l,r = 0, len(arr)-1

    while l <= r:
        mid = (l+r)//2

        if arr[mid] > arr[mid+1]:
            r = mid
        else:
            l = mid + 1
        
    return l

#---------------------------------------------------------------------------------------

#Binary Search
#Find Single Element
def singleElement(arr):
    n = len(arr)

    if n == 1 or arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    
    l,r = 1, n-2

    while l <= r:

        mid = (l+r)//2

        if arr[mid] != arr[mid+1] and arr[mid] != arr[mid-1]:
            return arr[mid]
        elif (mid%2==0 and arr[mid] != arr[mid+1]) or (mid%2==1 and arr[mid] != arr[mid-1]):
            l = mid + 1
        else:
            r = mid - 1
        
    return -1

#---------------------------------------------------------------------------------------

#Searching Single Element using XOR
def singleElementUsingXOR(arr):
    xor = 0

    for i in arr:
        xor ^= i
    
    return xor

#---------------------------------------------------------------------------------------

#Binary Search
#SquareRoot
def sqrtUsingBinarySearch(num):
    l,r = 0, num

    while l <= r:
        mid = (l+r)//2

        if mid*mid == num:
            return mid
        elif mid*mid > num:
            r = mid - 1
        else:
            l = mid + 1
    
    return -1

#---------------------------------------------------------------------------------------
#Binary Search
#Nth root of a number
def funct(mid,n,m):
    ans = 1

    for i in range(n):
        ans *= mid

        if ans > m:
            return 2
    if ans == m:
        return 1
    return 0

def nthroot(n,m):
    l,r = 1,m

    while l <= r:
        mid = (l+r)//2
        midn = funct(mid,n,m)

        if midn == 1:
            return mid
        elif midn == 2:
            r = mid -1
        else:
            l = mid + 1
    return -1


#---------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------

#finding the union
def unionOfTwoArray(arr1, arr2):
    i,j = 0, 0
    union = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    while i < len(arr1):
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1
    
    return union
#---------------------------------------------------------------------------------------
  
    


#largest Element in an Array
def largestElementInAnArray(arr):
    max = arr[0]

    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
        
    return max
#---------------------------------------------------------------------------------------


#to check if the array is sorted or not
def arraySortedOrNot(arr):
    count = 0

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            count += 1
        
    if count == 0:
        return True
    return False

#---------------------------------------------------------------------------------------

#remove duplicate from sorted Array
def removeDuplicateFromSortedArray(arr):
    i = 0

    for j in range(1,len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]

    return i + 1