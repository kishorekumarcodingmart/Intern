house = [2,3,2,4]

def findsol(house):
    if not house:
        return 0

    if len(house)<=3:
        return max(house)

    def helper(dp):
        # dp = [0] * len(house)
        # dp[0] = house[0]
        dp[1] = max(dp[0],dp[1])

        for i in range(2,len(dp)):
            dp[i] = max(dp[i-1],dp[i] + dp[i - 2])

        return dp[-1]

    
    p1 = helper(house[:len(house)-1])
    p2 = helper(house[1:])
    return max(p1,p2)

print(findsol(house))