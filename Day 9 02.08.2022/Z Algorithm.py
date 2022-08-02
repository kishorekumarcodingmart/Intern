txt = "abcdabcaaabc"

find = "abc"

holestr = find + "$" + txt



for i in range(len(holestr)):
    count = 0
    if holestr[0]==holestr[len(find)+1]:
        count+=1
        i=0
        while(holestr[i]==holestr[len(find)+1+i]):
            print(holestr[i],holestr[len(find)+1+i])
            i+=1
