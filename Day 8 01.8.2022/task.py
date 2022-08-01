print()
mat  = [
    ['C','O','D','T','A','F'],
    ['G','R','I','R','F','K'],
    ['X','A','N','E','A','E'],
    ['G','N','G','E','F','K'],
    ['F','G','M','A','R','T'],
    ['T','E','L','M','P','Z']
]

words = ["CODINGMART","PEN","TREE","CAT","ORANGE","TREE"]

r = 6
c = 6


def findsol(mat,txt,i,j,r,c,level):
    if i>=r or j>=c or i<0 or j <0:
        return False

    if mat[i][j]!=txt[level]:
        return False

    if level==len(txt)-1:
        return True

    result = (findsol(mat,txt,i+1,j,r,c,level+1) or #down
                findsol(mat,txt,i,j+1,r,c,level+1) or #right
                findsol(mat,txt,i-1,j,r,c,level+1) or #up
                findsol(mat,txt,i,j-1,r,c,level+1) #left
            )

    if result==True:
        return True

    return False



final = False
output = []
for word in words:
    # print(word)
    for i in range(r):
        for j in range(c):
            if mat[i][j]==word[0]:
                if word not in output:
                    final = findsol(mat,word,i,j,r,c,0)
                    if final==True:
                        output.append(word)
                else:
                    continue


print(output)
print()