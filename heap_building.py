class Heap():

	def __init__(self, unsorted=[], top=True):
		self.heap = self.build_heap_from_top(unsorted) if top else self.build_heap_from_bottom(unsorted)

	def build_heap_from_top(self, unsorted):
		
		heap = []
		while len(unsorted_array) > 0:
			child = unsorted_array.pop()
			if child:
				heap.append(child)
				childindex = (len(heap) - 1)
				# parent = childindex/2, round down (int)
				parentindex = int(childindex/2)
				while (parentindex >= 0 and heap[parentindex] < child):
					heap[childindex] = heap[parentindex]
					heap[parentindex] = child
					childindex = parentindex
					parentindex = int(childindex/2)
		return heap

	def build_heap_from_bottom(self, unsorted):

		heap = unsorted
		# In place - we check right child, then left, then go up a level
		maxindex = len(heap) - 1
		checker = maxindex

		while checker > 0:
			left_child = checker * 2
			right_child = checker * 2 + 1
			if (maxindex >= heap[right_child] and heap[checker] < heap[right_child]):
				swp = heap[checker]
				heap[checker] = heap[right_child]
				heap[right_child] = swp
			elif (maxindex >= heap[left_child] and heap[checker] < heap[left_child]):
				swp = heap[checker]
				heap[checker] = heap[left_child]
				heap[left_child] = swp
			checker -= 1

		return heap

	def heap_sort(self):

		heap = self.heap
		limit = len(heap) - 1

		while limit > 0:

			# Take from root, put into new limit spot
			swp = heap[0]
			heap[0] = heap[limit]
			heap[limit] = swp
			limit -= 1

			# Fix new root placement
			newroot = 0

			while ((newroot*2 + 1) < limit and (heap[newroot] < heap[(newroot*2 + 1)] or heap[newroot] < heap[(newroot*2 + 2)])):

				# Left is larger than right; we pass newroot to left side
				if heap[(newroot*2 + 1)] >= heap[(newroot*2 + 2)]:
					swp = heap[newroot]
					heap[newroot] = heap[newroot*2 + 1]
					heap[newroot*2 + 1] = swp
					newroot = newroot*2 + 1
				else: # Pass to the right
					swp = heap[newroot]
					heap[newroot] = heap[newroot*2 + 2]
					heap[newroot*2 + 2] = swp
					newroot = newroot*2 + 2
		return heap

	def print(self):
		print('-------------------------')
		reversed_heap = self.heap
		reversed_heap.reverse()
		level = 0
		while len(reversed_heap) > 0:
			printLevel = []
			while len(reversed_heap) > 0 and len(printLevel) < pow(2,level):
				value = reversed_heap.pop()
				printLevel.append(value)
			level += 1
			print(printLevel)
		print('-------------------------')

unsorted_array = [5,3,4,2,45,67,12,13,2,3,55,43,1,0,7]

# Unsorted array * (at worst) 
ex = Heap(unsorted_array)
# ex.print()

ex2 = Heap(unsorted_array, False)
# ex2.print()

print(ex.heap_sort())
 