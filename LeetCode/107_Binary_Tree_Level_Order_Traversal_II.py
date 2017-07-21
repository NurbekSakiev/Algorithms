class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        res = []
        q = [root]
        while q:
            newList = []
            n = len(q)
            for i in range(n):
                t = q.pop()
                if t.left:
                    q.insert(0, t.left)
                if t.right:
                    q.insert(0, t.right)
                newList.append(t.val)
            res.insert(0, newList)
        return res