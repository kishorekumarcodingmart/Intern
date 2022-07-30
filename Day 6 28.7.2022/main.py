class Solution():
	def maxHist(self, row):
		result = []

		top_val = 0

		max_area = 0

		area = 0
		i = 0

		while (i < len(row)):
			if (len(result) == 0) or (row[result[-1]] <= row[i]):
				result.append(i)
				i += 1
			else:
				top_val = row[result.pop()]
				area = top_val * i

				if (len(result)):
					area = top_val * (i - result[-1] - 1)
				max_area = max(area, max_area)

		while (len(result)):
			top_val = row[result.pop()]
			area = top_val * i
			if (len(result)):
				area = top_val * (i - result[-1] - 1)

			max_area = max(area, max_area)

		return max_area

	def maxRectangle(self, A):
		result = self.maxHist(A[0])

		for i in range(1, len(A)):
			for j in range(len(A[i])):
				if (A[i][j]):
					A[i][j] += A[i - 1][j]

			result = max(result, self.maxHist(A[i]))

		return result



R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

A = []
print("Enter the entries rowwise:")


for i in range(R):          
    a =[]
    for j in range(C):   
         a.append(int(input()))
    A.append(a)

ans = Solution()

print(ans.maxRectangle(A))


