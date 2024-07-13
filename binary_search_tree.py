class Node(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.subtreesize = 1
		self.left=left
		self.right=right

class BinarySearchTree(object):

	def __init__(self, tree=[]):
		self.tree = self.construct(tree)

	def construct(self, input):
		# Straightforward, just build from root
		root = input.pop()
		tree = Node(root, None, None)
		while len(input) > 0:
			new = input.pop()
			cur = tree
			while cur:
				cur.subtreesize += 1;
				if new <= cur.val:
					if cur.left:
						cur = cur.left
						continue
					else:
						cur.left = Node(new, None, None)
						break
				elif new > cur.val:
					if cur.right:
						cur = cur.right
						continue
					else:
						cur.right = Node(new, None, None)
						break
		return tree

	def _inOrderTraversal(self, root):
		if root.val:
			if root.left:
				self._inOrderTraversal(root.left)
			print(root.val)
			if root.right:
				self._inOrderTraversal(root.right)

	def inOrderTraversal(self):
		return self._inOrderTraversal(self.tree)

	# O(logn) time to search (height of tree -- avg log(n), worst case (n))
	def search(self, search):
		return self._search(self.tree, search)

	def _search(self, check, search):
		if check.val:
			print(check.val == search)
			if check.val == search:
				return check
			elif check.val > search and check.left: # Go left
				return self._search(check.left, search)
			elif check.val < search and check.right: # Go right
				return self._search(check.right, search)
			else:
				return 'not found'

	# todo - Idk if list structure can support this per se
	# O(logn) time to insert as well (same as above)
	def insert(self, insert):
		check = 0
		while (check < (len(self.tree) - 1)):
			if self.tree[check] > search: # Go right
				check = check*2 + 1
			elif self.tree[check] < search: # Go left
				check = check*2
		# Accessed empty node
		self.tree[check] = insert

	'''
	def delete(self, search):
		return self._delete(self.tree, search)

	def _delete(self, check, search):

		value = self._search(check, search)

		if value != 'not found':
			# Predecessor - would be go left, then all the way right
			# Successor - would be go right, then all the way left
			# Either one works fine
			if not value.right and value.left:
				value = value.left # Replace entire node with left node
				# NEED TO DECREMENT PARENT :(
			elif value.right:
				successor = value.right
				while successor.left:
					successor.subtreesize -= 1
					successor = successor.left
				value.val = sucessor.val
				self._delete(sucessor, successor.val)
	'''
	def rank(self, val, tree):
		if not tree.val:
			return 1
		elif tree.val == val:
			return tree.left.subtreesize + 1
		elif tree.val > val: # Going left
			return self.rank(val, tree.left)
		elif tree.val < val: # Going right
			return tree.left.subtreesize + 1 + self.rank(val, tree.right)

x = [50,20,22,25,24,20,40,45,29,30,26]

ex = BinarySearchTree(x)
print(ex.inOrderTraversal())
print(ex.rank(26, ex.tree))
print(ex.rank(20, ex.tree))
print(ex.rank(40, ex.tree))