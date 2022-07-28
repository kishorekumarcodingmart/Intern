def getspiral(mat):

	result = []

	if len(mat)==0:
		return result

	row_begin = 0

	row_end = len(mat) - 1

	col_begin = 0

	col_end = len(mat[0]) - 1

	while row_begin <= row_end and col_begin <= col_end:

		for i in range(col_begin, col_end+1):
			result.append(mat[row_begin][i])
		row_begin += 1

		for i in range(row_begin,row_end+1):
			result.append(mat[i][col_end])
		col_end -= 1

		if row_begin <= row_end:
			for i in range(col_end,col_begin-1,-1):
				result.append(mat[row_end][i])
		row_end -= 1

		if col_begin <= col_end:
			for i in range(row_end,row_begin-1,-1):
				result.append(mat[i][col_begin])
		col_begin += 1

	return result



row = int(input())
col = int(input())


mat = []

for i in range(row):          
    a =[]
    for j in range(col):      
        a.append(int(input()))
    mat.append(a)

final = getspiral(mat)

# print(final)

matrix = [ final[i:i+row] for i in range(0,len(final),col) ]

for i in matrix:
	print(*i)