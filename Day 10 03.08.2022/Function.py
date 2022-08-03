def inttobin(number):

    lst = []
    while (number > 0):
        lst.append(number%2)
        number//=2 

    lst.reverse()
    return lst

print(inttobin(10))


def bintoint(number):
    ans = 0
    n = len(number)
    for i in range(n):
        ans += 2**(n-i-1) * number[i]
    return ans


print(bintoint([1,0,1,0]))