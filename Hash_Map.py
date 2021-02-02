class Hash_Table:
	def __init__(self):
		self.max = 100
		self.arr = [None for i in range(self.max)]

	def get_hash(self, key):
		h = 0
		for char in key:
			h += ord(char)
		return h % 100

	def add(self, key, val):
		h = self.get_hash(key)
		self.arr[h] = val

	def get_data(self, key):
		h = self.get_hash(key)
		return self.arr[h] 




t =Hash_Table()

t.add("Sajid", 1000)

valw = t.get_data("Sajid")


print(valw)