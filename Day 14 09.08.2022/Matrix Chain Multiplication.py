def findsol(lst):
    n = len(lst)

    dp = [[0 for i in range(n-1)] for j in range(n-1)]

    for a in range(n-1):
        for i in range(n-a-1):
            j = i+a
            if i==j:
                dp[i][j] = 0
            else:
                mini = 10000
                for k in range(i,j):
                    mini = min(mini , dp[i][k]+dp[k+1][j]+lst[i]*lst[k+1]*lst[j+1])
                dp[i][j] = mini
    # for i in dp:
    #    print(*i)
    # print()
    return dp[0][n-2]
    
lst = list(map(int,input().split()))

print()

print(findsol(lst))