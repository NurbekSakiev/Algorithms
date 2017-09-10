# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums or len(nums) == 0:
            return
        return self.helper(0, len(nums), nums)
        
    def helper(self, start, end, nums):
        if start >= end:
            return None
        maxIdx = None
        maxNum = float("-inf")
        for i in range(start, end):
            if maxNum < nums[i]:
                maxIdx = i
                maxNum = nums[i]
        
        newRoot = TreeNode(maxNum)
        newRoot.left = self.helper(start, maxIdx, nums)
        newRoot.right = self.helper(maxIdx + 1, end, nums)
        return newRoot