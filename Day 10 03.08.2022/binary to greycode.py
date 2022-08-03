n = int(input("Enter Binary Number : "))

binarynumber = bin(n)

binarynumberlist = []

for i in range(2,len(binarynumber)):
    binarynumberlist.append(int(binarynumber[i]))

greycode = [0]*len(binarynumberlist)

greycode[0] = binarynumberlist[0]

for i in range(len(greycode)-1,-1,-1):
    val = binarynumberlist[i] ^ binarynumberlist[i-1]
    greycode[i] = val


grey = ''.join(map(str, greycode))

print(int(grey,2))