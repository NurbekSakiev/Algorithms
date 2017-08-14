# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        res = []
        
        if not root:
            return res
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if not root.left and not root.right:
            res.append(root.val)
            return
        if root.left:
            self.helper(root.left, res)
        res.append(root.val)
        if root.right:
            self.helper(root.right, res)

# Solution 2

    def inorderTraversal(self, root):
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res