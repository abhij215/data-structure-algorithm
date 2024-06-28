def indexSearch(arr, target):
    if len(arr) > 1:
        for i in range(len(arr)):
            if arr[i] == target:
                return i
            
def recursionsearch(arr, target, N):

    ## base class
    if N == 0:
        return False
    
    if arr[0] == target:
        return True
    
    return recursionsearch(arr[1:], target, N-1)


if __name__ == "__main__":
    arr = [10,20,30,40]
    target = 20

    index = indexSearch(arr, target)
    print(index)