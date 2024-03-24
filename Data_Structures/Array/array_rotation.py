
def reverseArray(arr, start, end):
    if start>=end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverseArray(arr, start+1, end-1)


def rotateLeft(arr, high, d):
    if d == 0:
        return
    
    d = d % high

    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, high-1)
    reverseArray(arr, 0, high-1)

if __name__ == "__main__":

    arr = [10,12,23,34,45,56,67,78]
    d = 2
    ln = len(arr)

    print(arr)

    rotateLeft(arr, ln, d)

    print(arr)
