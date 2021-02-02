class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next
		

class Linked_List:
	def __init__(self):
		self.head = None

	

	def print_list(self):
		itr = self.head
		while itr:
			print(itr.data)
			itr = itr.next

	def insert_at_begining(self, data):
		node = Node(data, self.head)
		self.head = node

	def inser_at_end(self, data):
		if self.head is None:
			self.head = Node(data, None)

		itr = self.head
		while itr.next:
			itr = itr.next
		itr.next = Node(data, None)

	

	def inser_values(self, data_list):
		


		self.head = None
		for data in len(data_list):
			self.inser_at_end(data)

	def get_length(self):
		count = 0
		itr = self.head 
		while itr:
			count += 1
			itr = itr.next
		
		return count

	def remove_at(self, index):
		if index < 0 or index >= self.get_length():
			raise Exception("Invalid index")

		if index == 0:
			self.head = self.head.next
			return

		count = 0
		itr = self.head
		while itr:
			count == index - 1
			itr.next = itr.next.next
			break
			itr = itr.next
			count += 1
	def insert_at(self, index, data):
		itr = self.head
		if index < 0 or index > self.get_length():
			raise Exception("Invalid index")

		if index == 0:
			self.insert_at_begining(data)

		count = 0
		while itr:
			if count == index - 1:
				node = Node(data, itr.next)
				itr.next = node
				break
			itr = itr.next
			count += 1

	def  search(self, item):
		itr = self.head
		fount = False
		while itr is not None and not fount:
			if itr.data is item:
				fount = True
				break
			else:
				itr = itr.next

		print(fount)



link = Linked_List()
# You can insert at begining
link.inser_values([4, 5, 6, 7, 8])

link.print_list()