class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        if not left or not right:
            return left == right
        
        if left.val != right.val:
            return False
        
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)


# Solution 2

    def isSymmetric(self, root):
        if not root:
            return True
        q = [root.left, root.right]
        while q:
            r = q.pop()
            l = q.pop()
            if not r and not l: continue
            if not r or not l: return False
            if r.val != l.val: return False
            q.append(l.left)
            q.append(r.right)
            q.append(l.right)
            q.append(r.left)
        
        return True