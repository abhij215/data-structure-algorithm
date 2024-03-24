# searching in a sorted array
def binarySearch(arr, low, high, target):

    if high>=1:
        mid = low + (high-low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearch(arr, low, mid-1, target)
        else:
            return binarySearch(arr, mid+1, high, target)
    elif high == 0:
        return high
    else:
        return -1


def deleteElement(arr, target):
       
    index = binarySearch(arr, 0, len(arr)-1, target)
    del arr[index]
    return arr


    #print(index)


if __name__ == "__main__":

    list = [10,20,30,40,50,60,70,80]
    high = len(list)
    target = 10
    deleteNum = 40

    index = binarySearch(list, 0, high-1, target)
    print(index)

    deleteElement(list, deleteNum)
    print(list)

