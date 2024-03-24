def floor(arr, x):
    i,j = 0, len(arr)-1
    while i <= j:
        mid = (i+j)//2
        if arr[mid] < x:
            i = mid
        else:
            j = mid -1
    return i

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    floorv = floor(arr, 5)
    print(floorv)