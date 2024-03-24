
def mif(mid,n,m):
    ans = 1

    for i in range(n):
        ans *= mid

        if ans > m:
            return 2
    
    if ans == m:
        return 1
    
    return 0

def NthRoot(n: int, m: int) -> int:
    # 'ans' variable stores the
    # nth root of m
    ans = -1
    # 's' and 'e' are the lower and upper
    # bounds of our search space
    s = 1
    e = m
    while s <= e:
        mid = (s + e) // 2
        # 'x' stores the value of
        # mid ^ n
        x = 1
        # Iterating from '1' from 'n'
        # to get 'mid ^ n'
        for i in range(1, n + 1):
            x *= mid
            # If 'x' is greater than 'm'
            # it's better to stop the loop
            # as obviously, multiplying
            # x, further with 'mid' will increase it
            # more.
            if x > 1 * m:
                break
        # If 'x' becomes 'm', we have found the answer
        if x == 1 * m:
            ans = mid
            break
        # If 'x' is greater than 'm',
        # we should shift our search space
        # to lower integer values, otherwise higher.
        if x > m:
            e = mid - 1
        else:
            s = mid + 1
    return ans




def nthroot(n,m):
    l,r = 1,m

    while l <= r:
        mid = (l+r)//2
        midn = mif(mid,n,m)

        if midn == 1:
            return mid
        elif midn == 2:
            r = mid - 1
        else:
            l = mid + 1
    return -1


if __name__ == "__main__":
    N,M = 3, 27

    print(nthroot(N,M))

