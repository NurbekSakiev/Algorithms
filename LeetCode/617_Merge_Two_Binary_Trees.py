# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def mergeTrees(self, t1, t2):
        
        if not t1:
            return t2
        if not t2:
            return t1
    
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


# Solution 2

    def mergeTrees(self, t1, t2):
        
        if not t1:
            return t2
        if not t2:
            return t1
        st = [[t1,t2]]
        
        while st:
            t = st.pop()
            if t[0] == None or t[1] == None:
                continue
            t[0].val += t[1].val
            if not t[0].left:
                t[0].left = t[1].left
            else:
                st.append([t[0].left, t[1].left])
            if not t[0].right:
                t[0].right = t[1].right
            else:
                st.append([t[0].right, t[1].right])
        return t1

