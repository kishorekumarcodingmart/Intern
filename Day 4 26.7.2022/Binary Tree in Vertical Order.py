class BST:
    def __init__(self,key,hd):
        self.key = key
        self.hd = hd
        self.lchild = None
        self.rchild = None

    def insert(self,data,hd):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data,hd-1)
            else:
                self.lchild = BST(data,hd-1)
        else:
            if self.rchild:
                self.rchild.insert(data,hd+1)
            else:
                self.rchild = BST(data,hd+1)

        
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        if self.hd not in d:
            d[self.hd] = []
        d[self.hd].append(self.key)
        # print(self.key,"->",self.hd)
        if self.rchild:
            self.rchild.inorder()


d = {}

root = BST(None,0)


# list1 = [10,6,3,1,6,98,3,7]

# list1 = []
list1 = [50,30,20,10,40,70,60,90]

# while True:
#     val = int(input())
#     if val<0:
#         break
#     else:
#         list1.append(val)

for i in list1:
    root.insert(i,0)

root.inorder()

for i in d:
    print(i, d[i])



