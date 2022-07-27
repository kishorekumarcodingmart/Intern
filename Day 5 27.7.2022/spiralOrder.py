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

mat = [
	[1,2,3,4,5],
	[6,7,8,9,10],
	[11,12,13,14,15],
	[16,17,18,19,20],
	[21,22,23,24,25]
]


final = getspiral(mat)

print(final)