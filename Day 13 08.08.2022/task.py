currency = [1,2,5]

amount = 11

def findsol(currency, amount):

    for c in reversed(currency) :
        if amount >= c :
            return [(amount // c, c),] + findsol( currency, amount % c )

    return []

lst = findsol( currency, amount )

for i in lst:
    print(str(i[1]) * i[0],end="")

print()
    