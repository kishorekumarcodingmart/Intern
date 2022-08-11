
def findsol(arr):
    lst = [1] * len(arr)


    for i in range(len(arr)-1,-1,-1):
        for j in range(i+1,len(arr)):
            if arr[i] < arr[j]:
                lst[i] = max(lst[i], 1 + lst[j])

    return max(lst)


print(findsol([0,1,0,3,2,3]))
