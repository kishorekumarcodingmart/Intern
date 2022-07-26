class node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class linkthelist:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("Linked is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    
    def add_end(self,data):
        new_node = node(data) 
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print("Item is Present in the List")
        else:
            new_node = node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data==x:
            new_node = node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n = n.ref 

        if n.ref is None:
            print("Node is not found!")
        else:
            new_node = node(data)
            new_node.ref = n.ref
            n.ref = new_node

        
         

linkedlist = linkthelist()

linkedlist.add_end(10)
linkedlist.add_end(20)
linkedlist.add_end(30)
linkedlist.add_end(40)


linkedlist.add_before(100 ,10)


linkedlist.display()