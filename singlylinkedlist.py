###### Singly Linked List ######
"""
- easy to insert, but hard to delete
- use sentinel node to avoid exception handling, but memory wasting when dealing with numerous tiny lists
- Here only implements an unsorted linked list, the sorted one is inferior to other data structure such as BST or heap
- Basic Operation:
1. Insert(S, x) : O(1)
2. Delete(S, x) : O(n)
3. Search(S, k) : O(n)
4. Maximum(S) : NOT IMPLEMENTED
5. Minimum(S) : NOT IMPLEMENTED
6. Successor(S, x) : NOT IMPLEMENTED
7. Predecessor(S, x) : NOT IMPLEMENTED
"""

# Universal Implementation (Naïve)
class Node:
	def __init__(self, key=None, val=None):
		self.key = key
		self.val = val # satelite data
		self.next = None

class SinglyLinkedList:
	def __init__(self):
		self.nil = Node() # sentinel node
		self.head = self.nil
		self.nil.next = self.head

	def insert(self, x):
		# head <- inserted node
		x.next = self.head
		self.head = x
		self.nil.next = x # sentinel node should always point to the head

	def delete(self, x):
		# assume x is in S
		prev = self.nil
		curr = self.head
		while curr != x:
			prev = curr
			curr = curr.next
		prev.next = x.next
		if x is self.head:
			self.head = x.next

	def search(self, key):
		curr = self.head
		while curr != self.nil:
			if curr.key != key:
				curr = curr.next
			else:
				return curr
		raise Exception("key not found")

# Array Inplementation
class Node:
	def __init__(self, key=None, val=None):
		self.key = key
		self.val = val # satelite data

class SinglyLinkedList:
	def __init__(self, maxsize):
		self.nil = Node()
		self.freestack = list(range(2, 2 * maxsize + 2, 2)) # first two spaces belong to sentinel node
		self.record = [None] * (2 * maxsize + 2) # each node takes 2 space ;  total # = maxsize + 1 (sentinel node)
		self.record[0] = self.nil
		self.record[1] = 0
		self.head = 0

	def insert(self, x):
		try:
			freeindex = self.freestack.pop()
		except IndexError:
			raise Exception("out of free space")
		else:
			self.record[freeindex] = x
			self.record[freeindex + 1] = self.head
			self.head = freeindex
			self.record[1] = self.head

	def delete(self, x):
		# assume x is in S
		prev = 0
		curr = self.head
		while self.record[curr] is not x:
			prev = curr
			curr = self.record[curr + 1]
		self.freestack.append(curr) # push deleted index back to free stack
		self.record[prev + 1] = self.record[curr + 1] # prev.next = curr.next
		if curr == self.head:
			self.head = self.record[curr + 1]

	def search(self, key):
		index = self.head
		while self.record[index].key != key:
			if not index:
				raise Exception("key not found")
			else:
				index = self.record[index + 1]
		return self.record[index]
