# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        if not root:
            return []
        res = []
        q = [root]
        
        while q:
            n = len(q)
            s = 0
            for i in range(n):
                node = q.pop()
                s += node.val
                if node.left:
                    q.insert(0, node.left)
                if node.right:
                    q.insert(0, node.right)
            res.append(float(s) / n)
        return res