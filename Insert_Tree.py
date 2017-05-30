# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def insertNode(self, head, node):
		if head == None:
			head = node
			head.left = head.right = None
		else:
			if head.val > node.val:
				if head.left == None:
					head.left = node
				else:
					self.insertNode(head.left, node)
			else:
				if head.right == None:
					head.right = node
				else:
					self.insertNode(head.right, node)

