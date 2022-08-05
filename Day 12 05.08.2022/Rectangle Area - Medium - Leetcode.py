
def find(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2):
    overlap = (max(min(ax2,bx2) - max(ax1,bx1),0) * 
    max(min(ay2,by2)-max(ay1,by1),0))
        
    return (ax1-ax2)*(ay1-ay2)+(bx1-bx2)*(by1-by2) - overlap


ax1 = int(input("ax1 : "))
ay1 = int(input("ay1 : "))
ax2 = int(input("ax2 : "))
ay2 = int(input("ay2 : "))


bx1 = int(input("bx1 : "))
by1 = int(input("by1 : "))
bx2 = int(input("bx2 : "))
by2 = int(input("by2 : "))

result = find(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2)

print(result)

