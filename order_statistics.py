# Order Statistics

# given unsorted array a, find k-th smallest element

# Concept: want to grab a value, pivot table, then sort thru smaller or larger
# Best complexity would be n log2 n (eg, n initial time, then log2 n by each halving)
# Worst would be n^2 (in case where each selection is only shaving off (n-1) and we essentially iterate thru n length n times)

ex = [100,123,450,777,555,455,344,233,111]
exEdge = []

def find_kth_smallest(a, k):
	# Pick a value at random
	i = 0

	if len(a) > 0:
		pivot = a[i]

		lower = []
		upper = []
		for j, val in enumerate(a):
			if j == i:
				continue
			elif val > pivot:
				upper.append(val)
			elif val < pivot:
				lower.append(val)
			# Add pivot-matching element at random to top or bottom list

		# Check if k-smallest (compare against lower) or k-largest (compare against upper)
		# 3rd smallest [1,2,3] x | len(lower) = 3 * so we want (len(lower) + 1)
		if (k) == (len(lower) + 1):
			return pivot;
		# If k is smaller index than given, hunt in lower list
		elif k < (len(lower) + 1):
			return find_kth_smallest(lower, k)
		# If k is larger index than given, hunt in upper list (scaled accordingly)
		# 4th smallest [1] x [2, 3, xxxx] (k - (len(lower) + 1 (for pivot)))
		# 3rd smallest [1] x [2, 3, etc] // 3 - (1+ 1) = 1
		elif k > (len(lower) + 1):
			return find_kth_smallest(upper, (k - len(lower) - 1))
	else:
		return 'empty search'


# [print(f"{exK}th placement is {find_kth_smallest(ex, exK)}") for exK in range(1, len(ex) + 1)]

# # Out-of-range
# [print(f"{exK}th placement is {find_kth_smallest(ex, exK)}") for exK in range(1, len(ex) + 4)]

# # 0th case (invalid)
# [print(f"{exK}th placement is {find_kth_smallest(ex, exK)}") for exK in range(0, len(ex))]

# # Empty list
# [print(f"{exK}th placement is {find_kth_smallest(exEdge, exK)}") for exK in range(1, 2)]


# # IN-PLACE -- something is wrong here TODO

# def find_kth_smallest_in_place(a, k):
# 	if (len(a) > 1):
# 		pivot = 0
# 		left = 1
# 		right = len(a) - 1
# 		while (left != right):
# 			while a[right] > a[pivot] and right > left:
# 				right -= 1
# 			while a[left] < a[pivot] and left < right:
# 				left +=1
# 			if (left != right):
# 				swp = a[right]
# 				a[right] = a[left]
# 				a[left] = swp
# 		# Finally, swap w pivot - we know it will be less than because right pointer touched it first
# 		# UNLESS - first value is smallest.
# 		if (a[pivot] > a[left]):
# 			swp = a[pivot]
# 			a[pivot] = a[left]
# 			a[left] = swp
# 		print('-----------------')
# 		print(f'finding {k}th from {a}, left is {left} with val {a[left]}, pivot is {a[pivot]}')

# 		# See if it matches our kth smallest
# 		if left == (k - 1):
# 			return a[left]
# 		elif left > (k - 1):
# 			return find_kth_smallest_in_place(a[:left], k)
# 		elif left < (k - 1):
# 			# [1,2,3] x [5, 6] #5th -> 1st so (k - len(a[:x]))
# 			return find_kth_smallest_in_place(a[left:], (k - len(a[:left])))
# 	else:
# 		return a[0] if a else 'N/A'


[print(f"{exK}th placement is {find_kth_smallest_in_place(ex, exK)}") for exK in range(1, (len(ex) + 1))]

# # # Out-of-range
# [print(f"{exK}th placement is {find_kth_smallest_in_place(ex, exK)}") for exK in range(1, len(ex) + 4)]

# # # 0th case (invalid)
# [print(f"{exK}th placement is {find_kth_smallest_in_place(ex, exK)}") for exK in range(0, len(ex))]

# # Empty list
# [print(f"{exK}th placement is {find_kth_smallest_in_place(exEdge, exK)}") for exK in range(1, 2)]

			


