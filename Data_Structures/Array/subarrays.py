
def subarray(arr, start, end):

    if end == len(arr):
        return
    elif start > end:
        return subarray(arr, 0, end + 1)
    else:
        print(arr[start:end+1])
        return subarray(arr, start+1, end)

if __name__ == "__main__":
    arr = [1,2,3,4]
    subarray(arr,0,0)