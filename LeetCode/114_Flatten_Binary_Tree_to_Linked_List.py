# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        if not root:
            return
        q = [root]
        head = None
        prev = None
        while q or head:
            
            if not head:
                head = q.pop()
            if prev:
                prev.right = head
            if not head.right and not head.left:
                prev = head
                head = None
                continue
            if head.right:
                q.append(head.right)
            head.right = head.left
            prev = head
            head.left = None
            head = head.right