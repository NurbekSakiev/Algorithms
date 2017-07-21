# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        q = [root]
        count = 1
        while q:
            n = len(q)
            newList = []
            for i in range(n):
                t = q.pop()
                if t.left:
                    q.insert(0, t.left)
                if t.right:
                    q.insert(0, t.right)
                if count %2 != 0:
                    newList.append(t.val)
                else:
                    newList.insert(0, t.val)
            count += 1
            res.append(newList)
        return res