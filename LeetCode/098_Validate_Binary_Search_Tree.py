# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        return self.helper(root, float("-inf"), float("inf")) 
        
    def helper(self, root, minimum, maximum):
        if not root:
            return True
        if root.val >= maximum or root.val <= minimum:
            return False
        return self.helper(root.right, root.val, maximum) and self.helper(root.left, minimum, root.val)