# Dynamic programming

# Given a grid of width w by depth d, how many paths to access (x, y)?

class PathCounting():

	def __init__(self, width=0, depth=0):
		# THIS IS NOT CORRECT - BREAKS
		# self.grid = [[0]*depth]*width
		self.grid = [[0 for y in range(0,depth)] for x in range(0,width)]

	def solve(self, x, y):
		# Treat this as a tree
		# We know that we are essentially building out w*d nodes max -- see that inner nodes overlap
		# So to build, start at top left, then move my way down thru each row
		# Kick off -- 0,0 should have 1 defaulted
		self.grid[0][0] += 1

		for i, col in enumerate(self.grid): # 
			for j, total in enumerate(col):
				above = self.grid[i][j-1] if j > 0 else 0
				left = self.grid[i - 1][j] if i > 0 else 0
				self.grid[i][j] += above + left
				print(f'[{i},{j}]={above}+{left}={self.grid[i][j]}')
				if (i == x and j == y):
					return self.grid[i][j]

		# Alternatively, could build, then just look up self.grid[x][y]

# ex = Solution(4,4)
# print(ex.solve(1,1))

# Given two strings, n and m, find longest (nonsequential) common subsequence
# eg ABCBDAB and BDCABA -> 4, with BDAB

# Don't want to find all subsequences in n and compare to m, all subsequences would be 0(2^n * m)
# Just the length?

class LCS():

	def __init__(self, A='', B=''):
		self.A = A
		self.B = B
		self.solution = [['' for y in range(0, len(B))] for x in range(0, len(A))]

	#Algorithm here is:
	# If the letters match, add 1 to the diagonal value
	# Else, we just push forward the max of adjacent values -- because NO REPEATS
	# EG, if AA is compared to BA -> comparing [1,1] would give us a LCS of 1. But We cannot use the A in BA to match against the 1st A in AA - or else we'd be double-using it
	# Hence, the adjacent (rather than diagonals) can only be passed forward if the current values _do not match_
	def solve(self):
		reverseA = [(i, a) for i, a in enumerate(self.A)]
		reverseA.reverse()
		reverseB = [(i, b) for i, b in enumerate(self.B)]
		reverseB.reverse()
		maxA = len(self.A) - 1
		maxB = len(self.B) - 1
		for (i, a) in reverseA:
			for (j, b) in reverseB:
				if a == b:
					self.solution[i][j] += (self.solution[i+1][j+1] if (i+1 <= maxA and j+1 <= maxB) else '') + a
				else:
					self.solution[i][j] += max((self.solution[i][j+1] if j+1 <= maxB else ''),(self.solution[i+1][j] if i+1 <= maxA else ''), key=len)
		# HERE - we get the actual substring length
		return self.solution[0][0][::-1]


y = 'BBABEGCCDX'
# ABCD -> 4

# ex = LCS(x,y)
# print(ex.solve())


# 2 WAYS of approaching this:
# 1) Do a solution list and compare against previous - eg, at j, we compare back j locations to find max
# 2) Do LCS on sorted version
class LIS():
	def __init__(self, S=''):
		self.S = S
		self.solution = [0 for x in range(0, len(S))]

	def solve(self):

		for i, val in enumerate(self.S):
			# Check against previous
			# for j, comp in enumerate(self.S[:i]):
			lis_set = [self.solution[j] for j, comp in enumerate(self.S[:i]) if comp < val]
			self.solution[i] = (max(lis_set) + 1) if len(lis_set) > 0 else 1

		# To find actual substring: start at longest value, then go backwards with -1 increments finding nearest
		# TODO - this is greedy algo no? Eg, 34345 will always take ones nearest 5
		j = self.solution.index(max(self.solution))
		counter = max(self.solution)
		solution = self.S[j]
		for i, tot in reversed(list(enumerate(self.solution[:j]))):
			if self.S[i] < solution[-1] and tot == (counter-1):
				counter -= 1
				solution += self.S[i]

		return solution[::-1]
		# return max(self.solution)

	def solve2(self):
		sortedS = ''.join(sorted([a for a in self.S]))
		lcs = LCS(self.S, sortedS)
		return lcs.solve()

	# From geeks4geeks - this is thru binary search tree on solution list
	# So basically at each index, find lists where last value is larger than current index
	# Replace that last value with this current one *IF prev-to-last is smaller OR ELSE just create new [currentindex]
	# if last value is smaller than current index, copy (DONT keep old) and add to new list
	# [2,3,1,2,5,4] # 2,3,5 or 2,3,4 or 1,2,5 or 1,2,4
	# start [[2]]
	# @3 -> [[2,3]] #scenarioB
	# @1 -> [[1], [2,3]] #scenarioA
	# @2 -> [[1,2], [2,3]]
	# @5 -> [[1,2,5], [2,3,5]]
	# @4 -> [[1,2,4], [2,3,4]]
	def solve3(self):
		self.solution = [[self.S[0]]]
		for x in range(1, len(self.S)):
			found = False
			for possible in self.solution:
				if possible[-1] > self.S[x] and (len(possible) == 1 or possible[-2] < self.S[x]):
					possible[-1] = self.S[x]
					found = True
				elif possible[-1] < self.S[x]:
					possible += self.S[x]
					found = True
			if not found:
				self.solution.append([self.S[x]])
		return ''.join(min(self.solution))
		# return self.solution

import time

x = 'ABAENDFRCEDABAENDFRCEDABAENDFRCEDABAENDFRCEDABAENDFRCED' # max = 5 'ABDFR'
ex = LIS(x)

t = time.process_time()
a = ex.solve()
e1 = time.process_time() - t
b = ex.solve2()
e2 = time.process_time() - e1
c = ex.solve3()
e3 = time.process_time() - e2

print(a, e1)
print(b, e2)
print(c, e3)