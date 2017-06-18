# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
      
        leftCount = self.count(root.left)
        if leftCount >= k:
            return self.kthSmallest(root.left, k)
        elif k > leftCount + 1:
            return self.kthSmallest(root.right, k - leftCount - 1)
        return root.val
    
    def count(self, root):
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)

Solution #2


global count
global number
class Solution(object):
    def kthSmallest(self, root, k):
        global count
        global number
        count = k
        self.helper(root)
        return number
    
    def helper(self, root):
        global count
        global number
        if root.left is not None:
            self.helper(root.left)
        count -= 1
        if count == 0:
            number = root.val
            return
        if root.right:
            self.helper(root.right)