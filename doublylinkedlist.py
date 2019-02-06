###### Doubly Linked List ######
"""
- extra space to store the pointer to previous node (c/w singly linked list)
- insert & delete both O(1) (c/w singly linked list : delete O(n))
- use sentinel node to avoid exception handling, but memory wasting when dealing with numerous tiny lists
- Here only implements an unsorted linked list, the sorted one is inferior to other data structure such as BST or heap
- Basic Operation:
1. Insert(S, x) : O(1)
2. Delete(S, x) : O(1)
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
		self.prev = self
		self.next = self

class DoublyLinkedList:
	def __init__(self):
		self.nil = Node() # sentinel node
		self.head = self.nil

	def insert(self, x):
		# head <- inserted node
		x.next = self.head
		x.prev = self.nil
		self.head.prev = x
		self.nil.next = x # sentinel node should always point to the head
		self.head = x

	def delete(self, x):
		# assume x is in S
		x.prev.next = x.next
		x.next.prev = x.prev
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

class DoublyLinkedList:
	def __init__(self, maxsize):
		self.nil = Node()
		self.freestack = list(range(3, 3 * maxsize + 3, 3)) # first three spaces belong to sentinel node
		self.record = [None] * (3 * maxsize + 3) # each node takes 3 space ;  total # = maxsize + 1 (sentinel node)
		self.record[0] = self.nil
		self.record[1] = 0 # default next attribute points to sentinel itself
		self.record[2] = 0 # default prev attribute points to sentinel itself
		self.head = 0

	def insert(self, x):
		try:
			freeindex = self.freestack.pop()
		except IndexError:
			raise Exception("out of free space")
		else:
			self.record[freeindex] = x
			self.record[freeindex + 1] = self.head
			self.record[freeindex + 2] = 0 # prev attribute of the new node points back to the sentinel
			self.head = freeindex
			self.record[1] = freeindex

	def delete(self, x_index):
		# x_index is regarded as the pointer to x
		nex = self.record[x_index + 1]
		pre = self.record[x_index + 2]
		self.record[pre + 1] = nex
		self.record[nex + 2] = pre
		if x_index == self.head:
			self.head = nex

	def search(self, key):
		index = self.head
		while self.record[index].key != key:
			if not index:
				raise Exception("key not found")
			else:
				index = self.record[index + 1]
		return self.record[index]
