# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        
        q = [root]
        
        while q:
            root = q.pop()
            if root.right:
                q.insert(0, root.right)
            if root.left:
                q.insert(0, root.left)
        return root.val


# Solution 2


    def findBottomLeftValue(self, root):
        
        q = [root]
        
        for node in q:
            q += filter(None, (node.right, node.left))
        return node.val