from collections import deque

class Stack:
	def __init__(self):
		self.stack = deque()

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		self.stack.pop()

	def peek(self):
		return self.stack[-1]

	def is_empty(self):
		return len(self.stack) == 0

	def size(self):
		return len(self.stack)

	def print_stack(self):
		print(self.stack)

newStack = Stack()




newStack.push("Sajid")
newStack.print_stack()


