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
        # Steps:
        # 1. Check if linked list is empty or not
        #   - if empty head = new_node
        # 2. Else
        #   - loop untill it reach last element
        new_node = node(data) 
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            # This loop will go to the last element
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            

linkedlist = linkthelist()

linkedlist.add_end(10)
linkedlist.add_end(20)
linkedlist.add_end(30)
linkedlist.add_end(40)



linkedlist.display()