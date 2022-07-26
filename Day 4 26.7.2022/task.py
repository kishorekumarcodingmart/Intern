s=input()
l=[]
l[:0]=s
sl=[]
r=int(input())

no_val=r+(r-2) 
no_col=(len(l)//no_val)
extra=len(l)-no_col*no_val

print(s,l)
no_col=no_col+1
print(len(l),no_val,no_col,extra)

for i in range(0,no_col):
    sl.append(l[(no_val*i):(i+1)*no_val])
print(sl)
for i in range(r):
    for j in sl:
        if len(j)>i+1:
            if i==0 :
                print(j[i],end='')
            elif i==(r-1):
                print(j[no_val//2],end='')
            else:
                print(j[i],j[no_val-i],sep='',end='')
        elif len(j)==i+1:
            print(j[i],end='')
    
