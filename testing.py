
def recsum(arr):

    if len(arr) == 1:
        return arr[0]
    
    ans = arr[0] + recsum(arr[1:])

    return ans

def recserach(arr,target,N):

    if N == 0:
        return False
    
    if arr[0] == target:
        return True
    
    return recserach(arr[1:], target, N-1)


def recurswap(arr, start, end):

    if start >= end:
        return
    
    arr[start], arr[end] = arr[end], arr[start]

    recurswap(arr, start+1, end-1)

def binarysearc(arr, target, l, r):

    mid = (l+r)//2

    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binarysearc(arr, target, l, mid-1)
    else:
        return binarysearc(arr, target, mid+1, r)

    return False    

def powerf(a,b):

    if b == 0:
        return 1
    
    if b == 1:
        return a
    
    ans = powerf(a, b//2)

    if b%2 == 1:
        return a * ans * ans
    else:
        return ans*ans

if __name__ == "__main__":
    a = 2
    b = 5

    ans = print(powerf(a,b))

    #print(ans)

    #arr = [3,1,5,7,12]
    #print(arr)

    #ans = binarysearc(arr, 5, 0, len(arr)-1)

    #print(ans)


    #print(len(arr[1:]))

    #recurswap(arr, 0, len(arr)-1)

    #print(arr)

    #target = 1

    #print(recserach(arr, target, len(arr)-1))