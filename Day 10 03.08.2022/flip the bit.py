import math

n = int(input())

binarynumber = bin(n)

binarynumber = int(binarynumber[2:])

binarynumberlen = math.ceil(math.log(n,2))

formula = ((2**binarynumberlen)-1)^n

print(formula)