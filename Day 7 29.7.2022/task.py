mat = [["C","O","D","F","S"],
        ["M","L","I","K","Q"],
        ["R","T","N","X","Z"],
        ["T","L","G","M","A"],
        ["X","L","Q","T","R"]
    ]

txt = "CODINGMART"

def findword(mat,txt,i,j,r,c,l):

    if mat[i][j]==" ":
        return False

    temp = mat[i][j]

    mat[i][j] = " "

    if l==len(txt):
        return True
    
    if mat[i][j]!=txt[l]:
        return False

    if i<0 or j<0 or i<=r or j <=c:
        return False

    check =  (findword(mat,txt,i+1,j,r,c,l+1) or 
    findword(mat,txt,i,j+1,r,c,l+1) or 
    findword(mat,txt,i-1,j,r,c,l+1) or 
    findword(mat,txt,i,j-1,r,c,l+1) )

    mat[i][j] = temp

    return check

final = False


def checkon():
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            if findword(mat,txt,i,j,len(mat[0]),len(mat),0):
                return True
    return False

print(checkon())
            



