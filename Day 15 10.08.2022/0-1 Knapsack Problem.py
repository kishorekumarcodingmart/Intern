def findsol(W, wt, val, n):
	dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0:
				dp[i][w] = 0
			elif wt[i-1] <= w:
				dp[i][w] = max(val[i-1]+ dp[i-1][w-wt[i-1]],dp[i-1][w])
			else:
				dp[i][w] = dp[i-1][w]
	for i in dp:
		print(*i)
	return dp[n][W]


val = [60, 100, 120]
wt = [10, 20, 30]

val = [1, 4, 5, 7]
wt = [1, 3, 4, 5]
W = 7
n = len(val)
print(findsol(W, wt, val, n))

