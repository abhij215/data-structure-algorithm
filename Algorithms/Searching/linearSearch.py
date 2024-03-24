def indexSearch(arr, target):
    if len(arr) > 1:
        for i in range(len(arr)):
            if arr[i] == target:
                return i


if __name__ == "__main__":
    arr = [10,20,30,40]
    target = 20

    index = indexSearch(arr, target)
    print(index)