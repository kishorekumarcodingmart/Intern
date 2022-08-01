mat = [["C","O","D","F","S"],
        ["M","L","I","K","Q"],
        ["R","T","N","X","Z"],
        ["T","L","G","M","A"],
        ["X","L","Q","T","R"]
    ]

# txt = "codingmart"

def findsiol(mat,txt,i,j,r,c,level):
    if i>=r or j>=c or i<0 or j <0 or mat[i][j]=="*":
        return False

    if mat[i][j]!=txt[level]:
        return False

    temp = mat[i][j]
    mat[i][j] = "*"

    if level==len(txt)-1:
        mat[i][j] = "*"
        return True

    result = (findsiol(mat,txt,i+1,j,r,c,level+1) or #down
                findsiol(mat,txt,i,j+1,r,c,level+1) or #right
                findsiol(mat,txt,i-1,j,r,c,level+1) or #up
                findsiol(mat,txt,i,j-1,r,c,level+1) #left
    )

    if result==True:
        mat[i][j]="*"
        return True

    mat[i][j] = temp
    return False



# R = int(input("Enter the number of rows:"))
# C = int(input("Enter the number of columns:"))

# A = []
# print("Enter the entries rowwise:")


# for i in range(R):          
#     a =[]
#     for j in range(C):   
#          a.append(input())
#     A.append(a)

# txt = input()

R = 5
C = 5
txt = "CODINGMART"

final = False

for i in range(R):
    for j in range(C):
        if mat[i][j]==txt[0]:
            final = final or findsiol(mat,txt,i,j,R,C,0)

for i in mat:
    print(*i)
print(final)

    

    

    

            



