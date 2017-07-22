# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        if not root:
            return []
        res = []
        q = [root]
        
        while q:
            n = len(q)
            maxNow = float('-inf')
            for i in range(n):
                t = q.pop()
                if t.right:
                    q.insert(0, t.right)
                if t.left:
                    q.insert(0, t.left)
                maxNow = max(maxNow, t.val)
            res.append(maxNow)
            
        return res

        515. Find Largest Value in Each Tree Row
        You need to find the largest value in each row of a binary tree.

# Solution 2

    def largestValues(self, root):
        res = []
        q = [root]
        
        while any(q):
            res.append(max(node.val for node in q))
            q = [kid for node in q for kid in (node.left, node.right) if kid]
        return res