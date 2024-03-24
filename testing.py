
def reverseUsingwhile(arr,start,end):

    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr

def rotataArray(arr,start,end,d):
    if d == 0:
        return
    
    d = d % len(arr)

    reverseUsingwhile(arr,start,d-1)
    reverseUsingwhile(arr,d,end)
    reverseUsingwhile(arr,start,end)


if __name__ == "__main__":

    arr = [1,2,3,4,5,6,7,8,9]
    start = 0
    end = len(arr)-1

    print(reverseUsingwhile(arr,start,end))

