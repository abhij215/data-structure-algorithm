
def checkPosibility(arr,dist,cows):
    n = len(arr)
    count = 1
    last = arr[0]

    for i in range(1,n):
        if arr[i] - last >= dist:
            count += 1
            last = arr[i]
        if count >= cows:
            return True
    return False


def minDis(arr,k):
    n = len(arr)
    arr.sort()
    limit = arr[n-1] - arr[0]

    for i in range(1,limit+1):
        if not checkPosibility(arr,i,k):
            return i-1
    return limit

def minimumDistUsingBinarySearch(arr,k):
    n = len(arr)
    arr.sort()
    low = 0
    limit = arr[n-1] - arr[0]

    while low <= limit:
        mid = (low+limit)//2

        if checkPosibility(arr,mid,k):
            low = mid + 1
        else:
            limit  = mid -1

    return limit


if __name__ == "__main__":
    stalls = [0, 3, 4, 7, 10, 9]
    k = 4

    print(minDis(stalls,k))
    print(minimumDistUsingBinarySearch(stalls,k))