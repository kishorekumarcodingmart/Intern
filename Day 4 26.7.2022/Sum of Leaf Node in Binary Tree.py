class BST:
    def __init__(self,key):
        self.key = key

        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def sumleaf(self):
        s = 0
        if self.lchild is None and self.rchild is None:
            return self.key
        if self.lchild:
            s+=self.lchild.sumleaf()
        if self.rchild:
            s+=self.rchild.sumleaf()
        return s

root = BST(None)



# list1 = [10,6,3,1,6,98,3,7]

list1 = []
# list1 = [10,5,2,7]

while True:
    val = int(input())
    if val<0:
        break
    else:
        list1.append(val)

for i in list1:
    root.insert(i)


print(root.sumleaf())
