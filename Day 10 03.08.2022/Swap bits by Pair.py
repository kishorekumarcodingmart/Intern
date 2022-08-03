number = 10

binarynumber = bin(number)

binarynumberlist = []

for i in range(2,len(binarynumber)):
    binarynumberlist.append(binarynumber[i])


def swap_bits(lst):
    n = len(lst)
    for i in range(n-1,0,-2):
        if i==0:
            break
        lst[i],lst[i-1] = lst[i-1],lst[i]
    
swap_bits(binarynumberlist)

swapbinaryval = ''.join(map(str, binarynumberlist))

print(int(swapbinaryval,2))