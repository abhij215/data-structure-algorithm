
def splitarray(arr,k):
    low = max(arr)
    high = sum(arr)

    while low <= high:
        mid = (low+high)//2
        if arraysum(arr,mid) > k:
            low = mid + 1
        else:
            high = mid - 1
    return low



def arraysum(arr,sum):
    n = len(arr)
    num = 1
    arraysumz = 0

    for i in range(n):
        if arraysumz + arr[i] <= sum:
            arraysumz += arr[i]
        else:
            num += 1
            arraysumz = arr[i]
    
    return num

def spilt_array(arr,k):
    low = max(arr)
    high = sum(arr)

    for i in range(low,high+1):
        if arraysum(arr,i) == k:
            return i
    return low




if __name__ == "__main__":
    arr = [1,2,3,4,5]
    k = 3

    result = spilt_array(arr,k)
    print(result)
    print(splitarray(arr,k))