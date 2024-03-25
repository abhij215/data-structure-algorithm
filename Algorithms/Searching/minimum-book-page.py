

def findStudent(arr,pages):
    student = 1
    n = len(arr)
    pageStudent = 0

    for i in range(n):
        if pageStudent + arr[i] <= pages:
            pageStudent += arr[i]
        else:
            student += 1
            pageStudent = arr[i]

    return student


def findPage(arr,n,m):

    if m > n:
        return -1
    
    low = max(arr)
    high = sum(arr)

    for pages in range(low, high+1):
        if findStudent(arr,pages) == m:
            return pages
    return low

def findPages(arr,n,m):

    if m > n:
        return -1
    
    low = max(arr)
    high = sum(arr)

    while low <=high:
        mid = (low+high)//2
        ans = findStudent(arr,mid)

        if ans > m:
            low = mid + 1
        else:
            high = mid - 1
    
    return low



if __name__ == "__main__":
    arr = [25, 46, 28, 49, 24]
    n = 5
    m = 4
    ans = findPage(arr, n, m)
    binar = findPages(arr,n,m)

    print('binary search result')
    print(binar)


    print(ans)