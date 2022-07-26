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

    def preordeer(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preordeer()
        if self.rchild:
            self.rchild.preordeer()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")

    def getHeight(self):

        if self.key:
            if self.lchild and self.rchild:
                return 1 + max(self.lchild.getHeight(),self.rchild.getHeight())
            elif self.lchild:
                return 1 + self.lchild.getHeight()
            elif self.rchild:
                return 1 + self.rchild.getHeight()
            else:
                return 1
        else:
            return 0

    def printlevel(self,lvl):
        if self.key==None:
            return
        if lvl==1:
            print(self.key,end=" ")
        elif lvl>1:
            if self.lchild is not None:
                self.lchild.printlevel(lvl-1)
            if self.rchild is not None:
                self.rchild.printlevel(lvl-1)
        

    def bfs(self):
        if self.key==None:
            return
        h = self.getHeight()
        for i in range(1,h+1):
            self.printlevel(i)

    def common(self,p,q):
        if self.key > max(p,q):
            return self.lchild.common(p,q)
        elif self.key < min(p,q):
            return self.rchild.common(p,q)
        else:
            return self.key






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

print("Pre Order")
root.preordeer()

print()
print("In Order")
root.inorder()

print()
print("Post Order")
root.postorder()

print()
print("BFS - Level order")
root.bfs()

print()


print(root.getHeight())

print(root.common(1,7))

print()

