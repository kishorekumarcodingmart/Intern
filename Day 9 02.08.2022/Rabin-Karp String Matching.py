

txt = "aabc"

find = "abc"

hashtotal = 0
k=0
for i in find:
    hashtotal += ord(i)*3**k
    k+=1

# print(hashtotal)
flag = False
c=0
for i in range(len(txt)-len(find)+1):
    hashnode = 0
    t = 0
    for j in range(i,i+len(find)):
        hashnode += ord(txt[j])*3**t
        t+=1
        # print(hashnode,hashtotal)
        # print(txt[j])
    if hashnode==hashtotal:
        flag = True
        c=c+1
        print(i)

if flag==True:
    print("Pattern Found")
else:
    print("Not Found")
        # break
    # print()
