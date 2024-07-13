# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Thru right-side transversal - we need 1, 3, 7
        

list_input = [1,2,3,4,5,6,7,8]


# Build a tree recursively:
def buildTree(node, list_input):
    if node:
        root = list_input.pop()
        # left
        left = list_input.pop()
        # right
        right = list_input.pop()
        node = TreeNode(root, left, right)
    return None

buildTree(None, list_input.reverse())