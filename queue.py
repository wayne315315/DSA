###### Queue ######
"""
- First In First Out (LIFO)
- Basic Operation:
1. Insert(S, x) : a.k.a. Enqueue/Put ; O(1)
2. Delete(S) : a.k.a. Dequeue/Get ; O(1)
3. Search : NOT IMPLEMENTED
4. Maximum : NOT IMPLEMENTED
5. Minimum : NOT IMPLEMENTED
6. Successor : NOT IMPLEMENTED
7. Predecessor : NOT IMPLEMENTED
"""

# Universal Implementation 
class MyQueue:
	def __init__(self, head, tail, maxsize=float('inf')):
		self.head = 0
		self.tail = 0
		self.size = maxsize
		self.array = [None] * (maxsize + 1)

	def put(self, x):
		if self.head == self.tail + 1:
			raise Exception("full queue")
		else:
			self.array[self.tail] = x
			if self.tail == self.size:
				self.tail = 0
			else:
				self.tail += 1

	def get(self):
		if self.head == self.tail:
			raise Exception("empty queue")
		else:
			x = self.array[self.head]
			if self.head == self.size:
				self.head = 0
			else:
				self.head += 1


# Python built-in Implementation : collections.deque, queue.Queue
from collections import deque # non-blocking but also thread-safe, simpler to use
q = deque() # maxsize=float('inf')
q.append(3) # put 3
q.append(4) # put 4
q.popleft() # get 3
q.popleft() # get 4
q.popleft() # queue empty : raise IndexError


from queue import Queue # default blocking, better use in multithreading scenario
q = Queue(maxsize=3)
q.put(4)
q.put(5)
q.get() # get 4
q.put(6)
q.put(7)
q.put(8) # queue empty : thread blocks until another thread retrieves from the queue
