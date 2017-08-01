class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start, end = 0, 0
        dic = {}
        maxLen = 0
        
        while end < len(s):
            if s[end] in dic:
                start = max(start, dic[s[end]] + 1)
            dic[s[end]] = end
            maxLen = max(maxLen, end - start + 1)
            end += 1
        return maxLen