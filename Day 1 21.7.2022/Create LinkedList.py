class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None 

class linked_list:
    def __init__(self):
        self.head = Node() 

    def addon(self,data): 
        new_node = Node(data)
        current = self.head

        while current.next!=None:
            current = current.next
        current.next = new_node

    def display(self):
        datalist = []
        addresslist = []
        current_node = self.head
        while current_node.next!=None:
            current_node = current_node.next
            datalist.append(current_node.data)
            addresslist.append(current_node)
        print(datalist)

myList = linked_list()

while True:
    num = int(input("Enter a Number : "))
    if num<0:
        break
    else:
        myList.addon(num)

    
myList.display()
