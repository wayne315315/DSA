###### Stack ######
"""
- Last In First Out (LIFO)
- Basic Operation:
1. Insert(S, x) : a.k.a. Push ; O(1)
2. Delete(S) : a.k.a. Pop ; O(1)
3. Search : NOT IMPLEMENTED
4. Maximum : NOT IMPLEMENTED
5. Minimum : NOT IMPLEMENTED
6. Successor : NOT IMPLEMENTED
7. Predecessor : NOT IMPLEMENTED
"""

# Universal Implementation 
class Stack:
	def __init__(self, maxsize=float("inf")):
		self.top = 0
		self.max = maxsize
		self.array = [None] * maxsize

	def push(self, x):
		if self.top  < self.max - 1:
			self.array[self.top] = x
			self.top += 1
		else:
			raise Exception("stack overflow")

	def pop(self):
		if self.top > 0:
			x = self.array[self.top]
			self.top -= 1
			return x
		else:
			raise Exception("stack underflow")


# Python built-in Implementation : list
stack = [] # maxsize = float("inf")
stack.append(3) # push element 3
stack.append("hey") # push element 4
x = stack.pop() # x = "hey"
y = stack.pop() # y = 3
stack.pop() # stack empty : raise IndexError