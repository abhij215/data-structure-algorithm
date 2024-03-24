

def insertIndex(arr, n, newIndex, newNum):

    for i in range(n-1, newIndex-1, -1):
        arr[i+1] = arr[i]
    arr[newIndex] = newNum



if __name__ == "__main__":

    arr = [10,20,30,40,50,90,-1,-1,-1,-1]
    n = 6
    ln = len(arr)

    newIndex = 2
    newNum = 25

    insertIndex(arr, n, newIndex, newNum)

    print(arr)