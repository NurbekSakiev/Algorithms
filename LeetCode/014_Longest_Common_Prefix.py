class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        pre = ""
        for i in range(len(strs[0])):
            pre = strs[0][:i+1]
            for j in range(1,len(strs)):
                if len(strs[j]) < len(pre) or strs[j][:i+1] != pre:
                    return pre[:-1]
        return pre