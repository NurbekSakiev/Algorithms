# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        newList = []
        self.inorder(root, newList)
        l,r = 0, len(newList) - 1

        while l < r:
            if newList[l] + newList[r] == k:
                return True
            elif newList[l] + newList[r] > k:
                r -= 1
            else:
                l += 1
        return False
    
    def inorder(self, root, newList):
        if not root:
            return
        self.inorder(root.left, newList)
        newList.append(root.val)
        self.inorder(root.right, newList)