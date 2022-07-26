rows = int(input("Enter number of rows: "))

n = 1
num = 1
temp = rows
for i in range(rows):
    for j in range(i):
        print(" ",end=" ")
    for j in range(rows-i):
        print(str(n**2) + " $", end=" ")
        n+=1

    for j in range(rows-i):
        print(str(temp*temp+num) + " $",end = " ")
        num+=1
    print()
    temp-=1