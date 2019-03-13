###### Heap ######
"""
- Heap property
1. Heap is a nearly complete binary tree, except for the right side of the bottom level
2. There are 2 kinds of common heaps : min-heap, max-heap
* min-heap : Given any node x, the key of its parent x.p.key <= the key of the node itself x.key
* max-heap : Given any node x, the key of its parent x.p.key >= the key of the node itself x.key
3. Heap is usually implemented with array.
4. Priority queue is usually implemented with heap. (ex. vanilla OS scheduler)
   Stable sort is achieved by comprison among tuples (priority, unique_count, task), instead of priority alone

- Basic Operation:
# h = θ(log(n)) is the height of the heap (nearly complete binary tree)
1. Insert(S, x) : a.k.a Push, O(log(n))
2. Delete(S) : a.k.a Pop, O(log(n))
3. Search(S, k) : NOT IMPLEMENTED
4. Maximum(S, x) : IMPLEMENTED IN max-heap, O(1)
5. Minimum(S, x) : IMPLEMENTED IN min-heap, O(1)
6. Successor(S, x) : NOT IMPLEMENTED
7. Predecessor(S, x) : NOT IMPLEMENTED

- Special Operation:
1. Heapify(T) : In-place heapify any nearly complete binary tree into min(max)-heap, O(n)
2. Sort(S) : In-place sorting, O(nlog(n))
"""
# Universal Implementation
class MinHeap:
	def __init__(self, array):
		self.heap = array
		self.size = len(array)
		self.heapify()

	def __str__(self):
		return str(self.heap)

	def __swap(self, i, j):
		temp = self.heap[i]
		self.heap[i] = self.heap[j]
		self.heap[j] = temp

	def __heapify_subtree(self, i):
		left = 2 * i + 1
		right = 2 * i  + 2
		if left < self.size and self.heap[left] < self.heap[i]:
			smallest = left
		else:
			smallest = i

		if right < self.size and self.heap[right] < self.heap[smallest]:
			smallest = right

		if i != smallest:
			self.__swap(i, smallest)
			self.__heapify_subtree(smallest)

	def heapify(self):
		for i in range(len(self.heap) // 2 - 1, -1, -1):
			self.__heapify_subtree(i)

	def push(self, x):
		self.heap.append(x)
		self.size += 1
		curr = self.size - 1
		p = (curr - 1) // 2
		while p >= 0 and self.heap[p] > self.heap[curr]:
			self.__swap(curr, p)
			curr = p
			p = (curr - 1) // 2

	def pop(self):
		self.size -= 1
		self.__swap(0, self.size)
		minimum = self.heap.pop()
		self.__heapify_subtree(0)
		return minimum

	def minimum(self):
		return self.heap[0]

	def sort(self):
		size = self.size
		while self.size:
			self.size -= 1
			self.__swap(0, self.size)
			self.__heapify_subtree(0)
		self.size = size
		start = 0
		end = self.size - 1
		# In-place reverse
		while start < end:
			self.__swap(start, end)
			start += 1
			end -= 1

# Python built-in Implementation : heapq
import heapq

a = [0, 3, 1, 5, 4, 2, 9, 6, 7, 8]
print("unsorted : ", a)

heapq.heapify(a)
print("heapified : ", a)

heapq.heappush(a, 2.5)
heapq.heappush(a, 1.3)
print("push 2.5 and 1.3 : ", a)

pop1 = heapq.heappop(a)
pop2 = heapq.heappop(a)
pop3 = heapq.heappop(a)
print("pop 3 times : %s, %s, %s" % (pop1, pop2, pop3))


