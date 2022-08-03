from itertools import permutations

check = [1,3,2]

List = list(permutations([1,2,3]))

if tuple(check) in List:
    h = List.index(tuple(check)) + 1
    print(list(List[h]))