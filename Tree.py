class TreeNode: 
	def __init__(self, data):
		self.data = data
		self.children = []
		self.parent = None



	def get_leve(self):
		leve = 0
		p = self.parent
		while p:
			leve += 1
			p = p.parent

		return leve


	def add_chid(self, child):
		child.parent = self
		self.children.append(child)


	def print_tree(self):
		space = ' ' * self.get_leve() * 3
		prefix = space + "|__" if self.parent else ""

		print(prefix + self.data)

		if self.children:
			for child in self.children:
				child.print_tree()


def build_product_tree():
	root = TreeNode("Electronics")



	laptop = TreeNode("laptop")
	laptop.add_chid(TreeNode("Mac"))
	laptop.add_chid(TreeNode("hp"))

	tv = TreeNode("Tv")
	tv.add_chid(TreeNode("Samsung"))
	tv.add_chid(TreeNode("viovo"))
	

	root.add_chid(laptop)
	root.add_chid(tv)

	return root


if __name__ == '__main__':
	root = build_product_tree()
	root.print_tree()
	