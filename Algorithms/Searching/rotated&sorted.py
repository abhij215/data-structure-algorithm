def pivotedSearch(arr, key):
    n = len(arr)-1

    pvt = findPivot(arr, 0, n)

    if pvt == -1:
        return binarySearch(arr, 0, n, key)

    if arr[pvt] == key:
        return pvt
    if arr[0] <= key:
        return binarySearch(arr, 0, pvt-1, key)
    return binarySearch(arr, pvt+1, n, key)



def findPivot(arr, low, high):

    if high < low:
        return -1

    if high == low:
        return low
    
    mid = (low+high)//2

    if mid > low and arr[mid] < arr[mid-1]:
        return mid - 1
    if mid < high and arr[mid] > arr[mid+1]:
        return mid
    if arr[low]>arr[mid]:
        return findPivot(arr, 0, mid-1)
    return findPivot(arr, mid+1, high)
    

def binarySearch(arr, low, high, key):

    if high < low:
        return -1
    
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1

def search(arr, low, high, key):
    if low > high:
        return -1
    
    mid = (low+high)//2

    if arr[mid] == key:
        return mid
    
    if arr[low] <= arr[mid]:

        if key >= arr[low] and key <= arr[mid]:
            return search(arr, low, mid-1, key)
        return search(arr, mid+1, high, key)
    
    if key >= arr[mid] and key <= arr[high]:
        return search(arr, mid+1, high, key)
    return search(arr, low, mid-1, key)

#direct search withput any pivot
def searchw(arr, target):
    l,r = 0, len(arr)-1

    while l<=r:
        mid = (l+r)//2

        if arr[mid] == target:
            return mid
        
        if arr[l] <= arr[mid]:
            if key >= arr[l] and key <= arr[mid]:
                r = mid -1
            else:
                l = mid+1
        else:
            if key >= arr[mid] and key<= arr[r]:
                l = mid + 1
            else:
                r = mid -1 



if __name__ == "__main__":
    arr = [5,6,7,8,9,10,0,1,2,3,4]

    key = 3

    idx = pivotedSearch(arr, key)
    print(idx)

    id2 = search(arr, 0, len(arr)-1, key)
    print(id2)

    id2 = searchw(arr, key)
    print(id2)