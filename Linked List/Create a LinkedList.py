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
            
linked_list = linkthelist()

linked_list.display()
            