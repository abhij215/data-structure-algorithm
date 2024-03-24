
def linearSearch(arr, ln, target):
    for i in range(ln-1):
        if arr[i] == target:
            return i
        else:
            return -1


if __name__ == "__main__":

    list = [10,20,30,40,50,60,70,80.90]
    ln = len(list)
    target = 10

    index = linearSearch(list, ln, target)

    if index == -1:
        print('no such element found')
    else:
        print(index)