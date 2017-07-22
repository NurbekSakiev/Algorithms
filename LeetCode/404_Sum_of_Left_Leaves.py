# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        tot = 0
        if root.left:
            if not root.left.left and not root.left.right:
                tot += root.left.val
            else:
                tot += self.sumOfLeftLeaves(root.left)
        tot += self.sumOfLeftLeaves(root.right)
        return tot