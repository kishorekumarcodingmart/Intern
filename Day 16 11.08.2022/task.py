def numWays(f, c):
    if c == 0 or f == 0:
        return 0

    if f == 1:
        return c

    same = 0
    diff = c 
    res = same + diff

    for i in range(2, f+1):
        same = diff
        diff = res * (c -1)
        res = same + diff

    return res


f = int(input("No of Fence : "))
c = int(input("No of Colors : "))

print(numWays(f,c))