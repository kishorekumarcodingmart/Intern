

arr = []

while True:
    temp = int(input())
    if temp <0:
        break
    else:
        arr.append(temp)

n = int(input())

position = -1

def findit(arr,n):
    i = 0
    while i<len(arr):
        if arr[i] == n:
            globals()['position'] = i
            return True
        i+=1

    return False

if findit(arr,n):
    print("Fount at",position)

else:
    print("Not Found")
