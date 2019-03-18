###### Trie ######
"""
- Trie property
1. Alias : Prefix tree, Radix tree, Digital tree
2. Trie is a tree with variable number of children for string comparison
   It is suited for spell checking, autocomplete, and lexicographic sorting.
3. Each node x has 2 attributes: x.children, x.val; x.key doesn't need to exist, x.val is for storing satellite data.
4. The value of the root node should be absent. i.e.  r.val = None
5. All descendants of a node x should have the common prefix of the associated string of x.
6. x.children can be implemented with hash table or singly linked list.
-- Hash table :  x.children = {'a': node1, 'b': node2, 'c': EOF}
-- Singly linked list : (char, child, next_sibling)   
7. Comparison between trie and hash table (TODO)

- Basic Operation
# m : the length of the string x
1. Insert(S, x) : O(m) if hash implementation ; O(m*|c|) if singly linked list where |c| is the size of char set
2. Delete(S, x) : O(m) if hash implementation ; O(m*|c|) if singly linked list where |c| is the size of char set
3. Search(S, x) : O(m) if hash implementation ; O(m*|c|) if singly linked list where |c| is the size of char set

- Advanced Operation
# sort : here sorting means lexicographic sorting, which definition is as follows
# Df : A string a=a0a1a2...ap is lesser than a string b=b0b1b2...bq if either one of the statements is True
-----> 1. there exists an integer j , st 0 <= j <= min(p,q),  aj < bj and ai == bi for i = 0, 1, ..., j-1
-----> 2. p < q and ai = bi for i = 0, 1, ..., p
1. sort(S, x) : return all strings in the dictionary containing the prefix x with lexicographic order.
   Only implemented in the one with singly linked list, not hash table.
"""

import heapq
from collections import defaultdict

# I1 - Singly linked list implementation
# worst case time complexity
# insert : O(m*|c|)
# delete : O(m*|c|)
# search : O(m*|c|)
# sort : O(N*|t|), where N is total number of matching strings, |t| is the maximal length of the remaining suffix
# worst case occurs when the substrings after prefix of all N matching strings are pairwise different among d-length prefix
# where d = log(N) // log(|c|)


class Node1:
	def __init__(self, key=None, val=None):
		self.key = key
		self.val = val
		self.next = None # pointer to next sibling
		self.child = None # pointer to the first child
		self.ref = 0

class Trie1:
	def __init__(self):
		self.root = Node1()

	def insert(self, s):
		if self.search(s):
			return
		curr = self.root
		curr.ref += 1
		for char in s:
			if not curr.child or char < curr.child.key:
				node = Node1(char)
				node.next = curr.child
				curr.child = node
				curr = node
				curr.ref += 1
				continue
			curr = curr.child
			while True:
				if curr.key == char:
					curr.ref += 1
					break
				elif not curr.next:
					curr.next = Node1(char)
					curr = curr.next
					curr.ref += 1
					break
				elif curr.next.key > char:
					node = Node1(char)
					node.next = curr.next
					curr.next = node
					curr = node
					curr.ref += 1
					break
				else:
					curr = curr.next
		if not curr.child or curr.child.key != "":
			null_c = Node1("")
			null_c.next = curr.child
			curr.child = null_c
						
	def delete(self, s):
		if not self.search(s):
			raise ValueError("string '%s' is not in the trie" % s)
		curr = self.root
		curr.ref -= 1
		for char in s:
			prev = None
			nxt = curr.child
			while True:
				if nxt.key == char:
					nxt.ref -= 1
					if nxt.ref == 0:
						if prev:
							prev.next = nxt.next
						else:
							curr.child = nxt.next
						return
					curr = nxt	
					break
				else:
					prev = nxt
					nxt = nxt.next
		curr.child = curr.child.next
		
	def prefix_search(self, prefix):
		curr = self.root
		for char in prefix:
			curr = curr.child
			while True:
				if not curr or curr.key > char:
					return
				elif curr.key == char:
					break
				curr = curr.next
		return curr

	def search(self, s):
		curr = self.prefix_search(s)
		if curr and curr.child.key == '':
			return curr

	def sort(self, s):
		strings = []
		node = self.search(s)
		if s == '':
			node = self.root

		def preorder(node, prefix):
			nonlocal strings
			child = node.child
			while child:
				char = child.key
				if char == '':
					strings.append(prefix)
				else:
					preorder(child, prefix + char)
				child = child.next
			
		if node:
			preorder(node, s)
		return strings

# I2 - Hash heap Implementation
# worst case time complexity
# insert : O(m*log|c|)
# delete : O(m + log|c|)
# search : O(m)
# sort : O(N*(|t| + log|c|)), where N is total number of matching strings, |t| is the maximal length of the remaining suffix
# worst case occurs when the substrings after prefix of all N matching strings are pairwise different among d-length prefix
# where d = log(N) // log(|c|)
class Node2:
	def __init__(self, val=None):
		self.children = {} # hash table
		self.keys = [] # heap
		self.waited = defaultdict(int) # for lazy key deletion
		self.val = val
		self.ref = 0

class Trie2:
	def __init__(self):
		self.root = Node2()

	def insert(self, s):
		if self.search(s):
			return 
		curr = self.root
		curr.ref += 1
		for char in s:
			if char not in curr.children:
				heapq.heappush(curr.keys, char)
				curr.children[char] = Node2()
			curr = curr.children[char]
			curr.ref += 1
		heapq.heappush(curr.keys, '') # Here '' represents null character
		curr.children[''] = len(s)
	
	def delete(self, s):
		if not self.search(s):
			raise ValueError("string '%s' is not in the trie" % s)
		curr = self.root
		curr.ref -= 1
		for char in s:
			nxt = curr.children[char]
			nxt.ref -= 1
			if nxt.ref == 0:
				curr.waited[char] += 1
				del curr.children[char]
				return
			else:
				curr = nxt
		heapq.heappop(curr.keys)
		del curr.children['']
	
	def prefix_search(self, prefix):
		curr = self.root
		for char in prefix:
			if char not in curr.children:
				return
			else:
				curr = curr.children[char]
		return curr
	
	def search(self, s):
		curr = self.prefix_search(s)
		if curr and '' in curr.children:
			return curr 

	def sort(self, s):
		strings = []
		node = self.prefix_search(s)

		if s == '':
			node = self.root

		def preorder(node, prefix):
			nonlocal strings
			valid_keys = []
			while node.keys:
				char = heapq.heappop(node.keys)
				if node.waited[char] > 0:
					node.waited[char] -= 1
					continue
				elif char == '':
					strings.append(prefix)
				else:
					preorder(node.children[char], prefix + char)
				valid_keys.append(char)
			node.keys = valid_keys

		if node:
			preorder(node, s)
		return strings


# Test zone
print("Singly linked list implementaion")
trie = Trie1()
trie.insert('cats')
trie.insert('cat')
trie.insert('dad')
trie.insert('')
trie.delete('cat')
trie.insert('cat')
trie.insert('cat')
trie.insert('cat')
trie.insert('cat')
trie.insert('cat')
trie.insert('cart')
trie.insert('catq')
trie.delete('cats')
trie.insert('ca')
print(trie.sort('cae'))
print(trie.sort(''))


print("Hash heap implementaion")
trie = Trie2()
trie.insert('cats')
trie.insert('cat')
trie.insert('dad')
trie.insert('')
trie.delete('cat')
trie.insert('cat')
trie.insert('cat')
trie.insert('cat')
trie.insert('cat')
trie.insert('cat')
trie.insert('cart')
trie.insert('catq')
trie.delete('cats')
trie.insert('ca')
print(trie.sort('cae'))
print(trie.sort(''))
