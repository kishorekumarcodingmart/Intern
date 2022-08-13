def findsol(txt,txtdict):

    dp = [True] + [False] * len(txt)

    for i in range(1,len(txt)+1):
        for word in txtdict:
            if dp[i - len(word)] and txt[:i].endswith(word):
                dp[i] = True
    return dp[-1]
    

txt = input("Enter the String : ")

txtdict = list(map(str,input("Enter the Array : ").split()))

print(findsol(txt,txtdict))
