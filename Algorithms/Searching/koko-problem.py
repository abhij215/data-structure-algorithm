import math

def totalHourToFinish(v, hour):
    totalHour = 0
    n = len(v)
    for i in range(n):
        totalHour += math.ceil(v[i]/hour)
    return totalHour

def minimumtimetoeat(v,h):
    r = max(v)
    for i in range(1,r):
        totalHour = totalHourToFinish(v,i)
        if totalHour <= h:
            return i        
    return r

def minimumTimeTaken(piles, h):
    l,r = 0, max(piles)

    while l <= r:
        mid = (l+r)//2

        if (sum(math.ceil(pile/mid) for pile in piles)) <= h:
            r = mid - 1
        else:
            l = mid + 1
        
    return l


if __name__ == "__main__":
    v = [7, 15, 6, 3]
    h = 8
    l = minimumtimetoeat(v,h)
    print(l)