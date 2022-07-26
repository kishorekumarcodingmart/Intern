
from itertools import permutations 
  
# arr = [7,4,6,8,2,3,1,2,3,5,4,2,3,1,1]

arr = [1,0,-1,0,-2,2]

total = 0

# total = 10


output = []

perm = permutations(arr,4) 
  
for i in list(perm):
    temp = list(i)
    if sum(temp)==total:
        if temp not in output:
            output.append(temp)

for i in output:
    print(i)


print(len(output))
        

    

