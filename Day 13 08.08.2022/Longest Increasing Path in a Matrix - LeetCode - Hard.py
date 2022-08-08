def longestIncreasingPath(matrix):
        n = len(matrix)

        m = len(matrix[0])

        dp = [[-1] * m for _ in range(n)]

        def dfs(i, j):
            if dp[i][j] != -1: 
                # print(dp[i],[j])
                return dp[i][j]
            

            dp[i][j] = 1
            for r,c in ((0,1),(0,-1),(1,0),(-1,0)):
                if 0 <= i+r < n and 0 <= j+c < m and matrix[i][j] < matrix[i+r][j+c]:
                    dp[i][j] = max(dp[i][j], 1 + dfs(i+r, j+c))
            # print(dp[i],[j])
            return dp[i][j]
            
        return max(max(dfs(i,j) for i in range(n)) for j in range(m))


mat = [
    [9,5,4,2,1],
    [8,7,6,3,4],
    [7,4,5,0,1],
    [3,2,4,3,1],
    [0,1,6,2,1]    
]


# for i in dp:
#     print(*i)
print(longestIncreasingPath(mat))