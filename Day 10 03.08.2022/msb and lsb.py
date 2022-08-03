number = int(input())

def findmsb(number):
    if number==0:
        return 0

    msb = 0
    number = int(number/2)

    while (number > 0):
        number = int(number/2)
        msb+=1

    return (1 << msb)

def findlsb(number):
    return number & 1


print(findmsb(number))
print(findlsb(number))