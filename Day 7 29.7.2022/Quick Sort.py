arr = []

while True:
    temp = int(input())
    if temp <0:
        break
    else:
        arr.append(temp)

def quick_sort(sequence):
    length = len(sequence)

    if length <=1:
        return sequence

    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for items in sequence:
        if items > pivot:
            items_greater.append(items)
        else:
            items_lower.append(items)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort(arr))
