def findsol(arr,amount):

    dp = [amount + 1] * (amount + 1)

    if amount<0:
        return -1

    dp[0] = 0

    for a in range(1,amount+1):
        for c in arr:
            if a - c >=0:
                dp[a] = min(dp[a],1+dp[a-c])
    
    if dp[amount] != amount +1:
        return dp[amount]
    else:
        return -1

arr = list(map(int,input("Enter the Weight : ").split(" ")))

amount = int(input("Enter the Amount : "))

print(findsol(arr,amount))