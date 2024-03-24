# function to add a new element
def addelement(arr, num):
    arr.append(num)

# function to delete an element
def deleteElement(arr, key):
    arr.remove(key)


if __name__ == "__main__":
    arr = [12,23,11,65,43,19,51]
    n = len(arr)
    num = 78
    delete = 12

    addelement(arr, num)
    print(arr)

    deleteElement(arr,delete)
    print(arr)

