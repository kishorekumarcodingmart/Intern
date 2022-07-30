position = -1

arr = []

while True:
    temp = int(input())
    if temp <0:
        break
    else:
        arr.append(temp)

n = int(input())

arr.sort()


def findval(arr,n):

    lower_bound = 0
    upper_bound = len(arr)-1

    while lower_bound <= upper_bound:

        mid = (lower_bound + upper_bound) // 2

        if arr[mid]==n:
            globals()['position'] = mid
            return True
        else:
            if arr[mid] < n:
                lower_bound = mid+1
            else:
                upper_bound = mid-1

    return False

if findval(arr,n):
    print('Found at',position)

else:
    print('Not Found')
