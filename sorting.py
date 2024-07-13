class Solution(object):

	def __init__(self, array=[]):
		self.array = array


	# Count the number of ns, in range 1-k, then reproduce with the count tallying them out
	def counting_sort(self):

		# Max value defined as k - we'd either get this as input, or access thru max() or maybe find with cursory search?
		k = max(self.array)
		sorted_freq_arr = [0] * (k+1)

		for n in self.array:
			sorted_freq_arr[n] += 1

		# UNPACK [c for b in a for c in b]
		packed = [[n]*freq for n, freq in enumerate(sorted_freq_arr)]
		return [c for b in packed for c in b]

	def quicksort(self, arr):
		# First - verify array:
		if (len(arr) > 1):
			# Take pivot, then sort on L and R
			pivot = arr[0]

			left = [x for x in arr[1:] if x <= pivot]
			right = [x for x in arr[1:] if x > pivot]

			return [*(self.quicksort(left)), pivot, *(self.quicksort(right))]
		else:
			return arr # If arr is [1] will get unpacked, if [], will not create None value

test_arr = [3,4,5,5,6,3,4,2,1,1,1,2,2,3,3,4,7,7,9,4,2]

x = Solution(test_arr)
print(x.quicksort(test_arr))

# // is FLOOR DIV -> rounds down, eg 11//5 = 2, -11//5 = -3