def findsol(amount,coins):
    dp = [0]*(amount+1)

    dp[0] = 1

    for c in coins:
        for a in range(1,amount+1):
            if a>=c:
                dp[a] = dp[a] + dp[a-c]
    return dp[-1]

arr = list(map(int,input("Enter the Weight : ").split(" ")))

amount = int(input("Enter the Amount : "))

print(findsol(amount,arr))