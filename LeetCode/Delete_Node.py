# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        if root == None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            
            minNode = self.helper(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)
        return root
        
    def helper(self, root):
        while root.left:
            root = root.left
        return root