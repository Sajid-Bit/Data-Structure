class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, data):
		self.data = data

	def setNext(self, next_data):
		self.next = next_data

class Linked_List:
	def __init__(self):
		self.head = None

	def is_emty(self):
		return self.head is None

	def add(self, data):
		new_node = Node(data)
		new_node.setNext(self.head)
		self.head = new_node

	def print_list(self):
		itr = self.head
		while itr:
			print(itr.getData())
			itr = itr.getNext()

	def size(self):
		itr = self.head
		count = 0
		while itr:
			count += 1
			itr = itr.getNext()
		print(count)

	def search(self, item):
		itr = self.head
		fount = False
		while itr is not None and not fount:
			if itr.getData() is item:
				fount = True
			else:
				itr = itr.next

		return fount
 




link = Linked_List()
link.add("Sajid")
link.print_list()
link.size()
i = link.search("Sajid")
print(i)























