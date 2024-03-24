"""Space complexity : O(1)
   Time Complexity : O(N)
"""
def reverseRecurrsion(arr, start, end):
    if start>=end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverseRecurrsion(arr, start+1, end-1)


"""Space complexity : O(1)
   Time Complexity : O(N)
"""
def reverseUsingwhile(arr,start,end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr

if __name__ == "__main__":
    arr = [10,20,45,21,93,85,65]
    start = 0
    end = len(arr)-1

    print(arr)

    reverseRecurrsion(arr, start, end)

    print(arr)