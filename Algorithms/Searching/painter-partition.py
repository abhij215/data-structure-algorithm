def numPartition(arr, partition):
    n = len(arr)
    painter = 1
    painting = 0

    for i in range(n):
        if painting + arr[i] <= partition:
            painting += arr[i]
        else:
            painter += 1
            painting = arr[i]
    return painter

def painterPartition(arr,k):
    low = max(arr)
    high = sum(arr)

    for i in range(low, high+1):
        if numPartition(arr,i) == k:
            return i
    return -1

def paintersPartition(arr,k):
    low = max(arr)
    high = sum(arr)

    while low <= high:
        mid = (low+high)//2
        if numPartition(arr,mid) > k:
            low = mid + 1
        else:
            high = mid - 1
    return low


if __name__ == "__main__":
    boards = [10, 20, 30, 40] 
    k = 2
    ans = painterPartition(boards,k)

    print(ans)

    print(paintersPartition(boards,k))
