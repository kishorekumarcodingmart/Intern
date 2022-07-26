class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_node(self, data):
        new_node = Node(data) 
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def display_list(self):
        if self.head is None:
            print("Linked is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.value,end=" ")
                n = n.next
        
    def delete_duplicates(self):

        current = self.head

        while current:
            runner = current
            # Check until runner.next is not None.
            while runner.next:
                if current.value == runner.next.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next




l = LinkedList()

while True:
    val = int(input())
    if val<0:
        break
    else:
        l.insert_node(val)


# l.display_list()
l.delete_duplicates()
print()
l.display_list()
print()


"""
Initialise 2 pointers(current and runner) to keep track of the previous and current node values
The current node is used for traversing through the linked list.
The runner node is used to compare the elements in the linked list.
"""