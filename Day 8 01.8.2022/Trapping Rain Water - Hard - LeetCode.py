
arr = []

while True:
    n = int(input())
    if n<0:
        break
    else:
        arr.append(n)



lenofarr = len(arr)

leftarr = [0]*lenofarr
leftarr[0] = arr[0]

rightarr = [0]*lenofarr
rightarr[lenofarr-1] = arr[lenofarr-1]

for i in range(1,lenofarr):
    leftarr[i] = max(arr[i],leftarr[i-1]) 

for i in range(lenofarr-2,-1,-1):
    rightarr[i] = max(arr[i],rightarr[i+1])


# print(leftarr)
# print(rightarr)

water = 0
for i in range(lenofarr):
    # print(min(leftarr[i],rightarr[i])-arr[i])
    water += min(leftarr[i],rightarr[i])-arr[i]

print(water)




