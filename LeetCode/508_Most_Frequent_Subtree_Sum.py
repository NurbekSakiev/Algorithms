# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def findFrequentTreeSum(self, root):
        res = []
        maxNum = 0
        dic = {}
        self.helper(root, dic)
        for k,v in dic.items():
            maxNum = max(maxNum, v)
        for k,v in dic.items():
            if v == maxNum:
                res.append(k)
        return res
        
    def helper(self, root, dic):
        if not root:
            return 0
        if not root.left and not root.right:
            dic[root.val] = 1 if root.val not in dic else dic[root.val] + 1
            return root.val
        totSum = root.val + self.helper(root.left, dic) + self.helper(root.right, dic)
        dic[totSum] = 1 if totSum not in dic else dic[totSum] + 1
        return totSum

# Solution 2

    def findFrequentTreeSum(self, root):
        if not root: return []
        
        def helper(root):
            if not root: return 0
            
            s = root.val + helper(root.left) + helper(root.right)
            dic[s] += 1
            return s
        
        dic = collections.Counter()
        helper(root)
        freq = max(dic.values())
        
        return [s for s in dic.keys() if dic[s] == freq]