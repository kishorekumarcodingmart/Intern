words = ["elephant","cat","trunk",
    "knife","table","book"]

# words = ["xa","ab","ac","ca"]

res = []

for i in words:
    temp = []
    temp.append(i)

    end = i[-1]

    for j in words:
        for k in words:
            if k[0] == end and k not in temp:
                temp.append(k)
                end = k[-1]



    res.append(temp)
    temp=[]


print(*res)
