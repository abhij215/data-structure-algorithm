def monoIn(arr,N):
    stk = []

    for i in range(N):

        while len(stk) > 0 and stk[len(stk)-1] > arr[i]:
            stk.pop()
        stk.append(arr[i])

    return stk

def monoDec(arr,N):
    stk = []

    for i in range(N):

        while len(stk) > 0 and stk[len(stk)-1] < arr[i]:
            stk.pop()
        stk.append(arr[i])

    return stk


if __name__ == "__main__":
    arr = [1, 4, 5, 3, 12, 10]
    N = len(arr)

    new = monoIn(arr, N)

    print(new)
