def sep(arr, n):

    if n == 0:
        return 0
    
    digit = n % 10
    n = n // 10

    sep(arr,n)

    print(arr[digit])

def powerf(a,b):

    if b == 0:
        return 1
    
    if b == 1:
        return a
    
    ans = powerf(a, b//2)

    if b%2 == 1:
        return a * ans * ans
    else:
        return ans*ans

if __name__ == "__main__":
    arr = ["zero", "one", "two", "three", "four","five", "six", "seven", "eight", "nine"]

    n = 432

    sep(arr, n) 