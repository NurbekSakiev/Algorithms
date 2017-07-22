# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	
	def levelOrder(self, root):
        
        q = [root]
        res = []
        
        while any(q):
            n = len(q)
            newList = []
            for i in range(n):
                t = q.pop()
                if t.left:
                    q.insert(0, t.left)
                if t.right:
                    q.insert(0, t.right)
                newList.append(t.val)
            res.append(newList)
        return res

# Solution 2

    def levelOrder(self, root):
        
        q = [root]
        res = []
        
        while any(q):
            res.append(list(map(lambda x: x.val, q)))
            q = [kid for node in q for kid in (node.left, node.right) if kid]
        return res