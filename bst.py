###### Binary Search Tree ######
"""
- Binary search tree property
Let x be a node in a binary search tree. 
If y is a node in the left subtree of x, then y.key <= x.key.
If y is a node in the right subtree of x, then y.key >= x.key


- Basic Operation:
# h is the height of the binary tree. h = O(log(n)) if balanced ; otherwise h = O(n)
# The implementation here doesn't guarantee the balance of BST
# Create a sentinel node as the common external leaves(childs of all internal leaves) and the parent of the root
1. Insert(S, x) : O(h)
2. Delete(S, x) : O(h)
3. Search(S, k) : O(h)
4. Maximum(S, x) : O(h)
5. Minimum(S, x) : O(h)
6. Successor(S, x) : O(h)
7. Predecessor(S, x) : O(h)

- Advanced Operation:
1. InOrderTraversal(S, x)
2. PreOrderTraversal(S, x)
3. PostOrderTraversal(S, x)
"""

# Universal Implementation
class Node:
	def __init__(self, key=None, val=None):
		self.key = key
		self.val = val
		self.p = self
		self.left = self
		self.right = self

class BST:
	def __init__(self):
		self.nil = Node()
		self.root = self.nil

	def insert(self, x):
		prev = self.nil
		curr = self.root
		# inserted node must be a new internal leave
		x.left = self.nil
		x.right = self.nil
		while curr is not self.nil:
			prev = curr
			if x.key < curr.key:
				curr = curr.left
			else:
				curr = curr.right
		x.p = prev
		if x.p is self.nil:
			self.root = x
			x.p.left = x
			x.p.right = x
		elif x.key < x.p.key:
			x.p.left = x
		else:
			x.p.right = x

	def delete(self, x):
		# most complicated operation
		if not x.left:
			self.transplant(x, x.right)
		elif not x.right:
			self.transplant(x, x.left)
		else:
			nex = self.minimum(x.right) # successor must be in the subtree of x, since both children exist
			if nex is not x.right:			
				self.transplant(nex, nex.right) # left child of nex = self.nil
				nex.right = x.right
				nex.right.p = nex
			self.transplant(x, nex)
			nex.left = x.left
			nex.left.p = nex

	def transplant(self, x, y):
		# replace subtree rooted at x with subtree rooted at y
		# y might be self.nil
		if x is self.root:
			self.root = y
		elif x is x.p.left:
			x.p.left = y
		else:
			x.p.right = y
		if y is not self.nil:
			y.p = x.p

	def search(self, key):
		curr = self.root
		while curr is not self.nil:
			if key == curr.key:
				return curr
			elif key < curr.key:
				curr = curr.left
			else:
				curr = curr.right
		raise Exception("key not found")

	def minimum(self, x):
		"""return the minimum of the subtree rooted at x"""
		prev = self.nil
		curr = x
		while curr is not self.nil:
			prev = curr
			curr = curr.left
		return prev

	def maximum(self, x):
		"""return the maximum of the subtree rooted at x"""
		prev = self.nil
		curr = x
		while curr is not self.nil:
			prev = curr
			curr = curr.right
		return prev

	def successor(self, x):
		if x.right is not self.nil:
			return self.minimum(x.right)
		else:
			curr = x
			while curr is not self.root:
				if curr.p.left is curr:
					return curr.p
				else:
					curr = curr.p
		raise Exception("no successor")

	def predecessor(self, x):
		if x.left is not self.nil:
			return self.maximum(x.right)
		else:
			curr = x
			while curr is not self.root:
				if curr.p.right is curr:
					return curr.p
				else:
					curr = curr.p
		raise Exception("no predecessor")

	def inorder(self, x):
		# In-order traversal among subtree rooted at x
		if x is self.nil:
			return
		else:
			self.inorder(x.left)
			print(x)
			self.inorder(x.right)

	def preorder(self, x):
		# Pre-order traversal among subtree rooted at x
		if x is self.nil:
			return
		else:
			print(x)
			self.preorder(x.left)
			self.preorder(x.right)

	def postorder(self, x):
		# Post-order traversal among subtree rooted at x
		if x is self.nil:
			return
		else:
			self.postorder(x.left)
			self.postorder(x.right)
			print(x)
