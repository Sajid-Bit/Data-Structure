class Binar_Tree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


	def add_child(self, data):
		if data == self.data:
			return None

		if data < self.data:
			if self.left:
				self.left.add_child(data)
			else:
				self.left = Binar_Tree(data)
		else:
			if self.right:
				self.right.add_child(data)
			else:
				self.right = Binar_Tree(data)

	def in_order_tr(self):
		elements = []

		if self.left:
			elements += self.left.in_order_tr()

		elements.append(self.data)

		if self.right:
			elements += self.right.in_order_tr()


		return elements

	def get_leve(self):
		leve = 0
		p = self.data
		while p:
			leve += 1
			p = p.parent

		return leve



	def serch(self, val):
		if self.data == val:
			return True


		if val < self.data:
			if self.left:
				self.left.serch(val)

			else:
				return False


		if val > self.data:
			if self.right:
				self.right.serch(val)


			else:
				return False







def build_tree(elements):
	root = Binar_Tree(elements[0])


	for i in range(1, len(elements)):
		root.add_child(elements[i])

	return root

if __name__ == '__main__':
	number = [90, 0, 9, 0, 3, 100, 67]
        


	number_tree = build_tree(number)

	h = number_tree.in_order_tr()
	for i in h:
		print(i.get_leve())

