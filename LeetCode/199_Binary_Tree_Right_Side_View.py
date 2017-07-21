# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        
        res = []
        q = [root]
        
        while any(q):
            res.append(q[-1].val)
            q = [kid for node in q for kid in (node.left, node.right) if kid]
        
        return res