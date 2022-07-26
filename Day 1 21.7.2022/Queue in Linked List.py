class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Queue:
	
	def __init__(self):
		self.front = self.rear = None

	def isEmpty(self):
		return self.front == None
	
	def EnQueue(self, item):
		temp = Node(item)
		
		if self.rear == None:
			self.front = self.rear = temp
			return
		self.rear.next = temp
		self.rear = temp

	def DeQueue(self):
		
		if self.isEmpty():
			return
		temp = self.front
		self.front = temp.next

		if(self.front == None):
			self.rear = None

q = Queue()

while True:
    num = int(input("Enter a Number : "))
    if num<0:
        break
    else:
        q.EnQueue(num)


q.DeQueue()

print("First Element : " + str(q.front.data))
print("Second Element : " + str(q.rear.data))
	
