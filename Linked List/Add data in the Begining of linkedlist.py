# To Create a Sigle Node which contains data and address
class node:
    def __init__(self,data):
        self.data = data
        self.ref = None

# To Link the All Sigle Node to a Linked List
# Initialy in head is none
class linkthelist:
    def __init__(self):
        self.head = None
    #display the linked this
    def display(self):
        # traversal 
        # 1. Check if linked list is Empty or not, if Empty print Empty list
        # 2. If its not Empty DO SOME FUNCTION!
        #Check if linked list is Empty
        if self.head is None:
            print("The Linked List is Empty")
        #iterate the linked list    
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
            
    #Append the node on the begining of the linked list
    # 1. Create a Node with data
    # 2. new_node.ref = head
    # 3. head = new_node
    def add_begin(self,data):
        # 1. Create Node with data
        new_node = node(data)
        # Now the node is created with data and ref as none
        # 2. new_node.ref = head
        new_node.ref = self.head
        # 3. head = new_node
        self.head = new_node
            
linked_list = linkthelist()

linked_list.add_begin(10)
linked_list.add_begin(20)
linked_list.add_begin(30)
linked_list.add_begin(40)



linked_list.display()
            