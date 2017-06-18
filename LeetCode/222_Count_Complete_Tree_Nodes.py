# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        l = r = root
        lh, rh = 0,0
        while l:
            l = l.left
            lh += 1
        while r:
            r = r.right
            rh += 1
        if lh == rh:
            return pow(2,lh) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# Solution #2

    def countNodes(self, root):
        if not root:
            return 0
        num = 1
        l = root.left
        r = root.left
        while r:
            l = l.left
            r = r.right
            num = num << 1
        if not l:
            return num + self.countNodes(root.right)
        else:
            return num + self.countNodes(root.left)
        