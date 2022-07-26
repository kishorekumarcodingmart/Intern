
class node:
	def __init__(self, x):
		self.data = x
		self.next = None

# To print	
def setData(head):
	tmp = head

	while (tmp != None):
		print(tmp.data)
		tmp = tmp.next

def getData(head, num):

	temp = node(-1)
	tail = head

	temp.data = num
	temp.next = None

	if (head == None):
		head = temp
		tail = temp

	else:
		while (tail != None):
			if (tail.next == None):
				tail.next = temp
				tail = tail.next
			tail = tail.next

	return head

def mergelists(head1,head2):

	tail = head1

	while (tail != None):
		if (tail.next == None
			and head2 != None):
			tail.next =head2
			break
		tail = tail.next

	return head1


head1 = node(-1)
head2 = node(-1)

head1 = None
head2 = None

head1 = getData(head1, 1)
head1 = getData(head1, 2)
head1 = getData(head1, 3)

head2 = getData(head2, 4)
head2 = getData(head2, 5)
head2 = getData(head2, 6)
head2 = getData(head2, 7)

head1 = mergelists(head1,head2)

setData(head1)

