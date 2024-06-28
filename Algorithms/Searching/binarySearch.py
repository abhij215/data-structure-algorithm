def binarySearch(arr,l,h,target):

    while l <= h:
        mid = l + (h-l)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            h =  mid - 1

def recusriveBinarySearch(arr, target, l, r):

    mid = (l+r)//2

    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return recusriveBinarySearch(arr, target, l, mid-1)
    else:
        return recusriveBinarySearch(arr, target, mid+1, r)
    
    return False



if __name__ == "__main__":
    arr = [10,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    target = 12
    index = binarySearch(arr,0,len(arr)-1,target)
    print(index)