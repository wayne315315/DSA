###### Segment Tree ######
"""
Support dynamic range minimum query with following methods
1. update(i, val) : O(log(n))
2. getmin(i, j) : O(log(n))
* segment tree : 2*n - 1 nodes
"""
class Segment:
	def __init__(self, array):
		# array : non-empty
		self.array = array
		self.size = len(array)
		self.mintree = [0] * (4 * self.size - 1) # the exact tree size = 2 ^ (ceil(log(n, 2)) + 1) - 1
		# build
		def build(index, l, r):
			if l == r:
				self.mintree[index] = self.array[l]
			else:
				mid = (l + r) // 2
				self.mintree[index] = min(build(2 * index + 1, l, mid), build(2 * index + 2, mid + 1, r))
			return self.mintree[index]
		build(0, 0, self.size - 1)
	def __update(self, index, l, r, i, val):
		if l <= i <= r:
			if l == r:
				self.mintree[index] = self.array[i] = val
			else:
				mid = (l + r) // 2
				self.mintree[index] = min(self.__update(2 * index + 1, l, mid, i, val), self.__update(2 * index + 2, mid + 1, r, i, val))
		return self.mintree[index]

	def update(self, i, val):
		self.__update(0, 0, self.size - 1, i, val)

	def query(self, i, j):
		if not 0 <= i <= j < self.size:
			return float('inf')
		if i == j:
			return self.array[i]
		mid = (i + j) // 2
		return min(self.query(i, mid), self.query(mid + 1, j))

seg = Segment([3,1,2,5,4,2,3,6,-2,9])
print(seg.array)
print(seg.mintree)
print("mininal value in array[1:7]", seg.query(1,6))
print("*** update ***")
seg.update(1, 3)
print(seg.array)
print(seg.mintree)
print("mininal value in array[1:7]", seg.query(1,6))
print("*** update ***")
seg.update(5, -1)
print(seg.array)
print(seg.mintree)
print("mininal value in array[1:7]", seg.query(1,6))
