class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start, end = 0, 0
        dic = {}
        maxLen = 0
        
        while end < len(s):
            dic[s[end]] = 1 if s[end] not in dic else dic[s[end]] + 1
            while start < end and dic[s[end]] > 1:
                dic[s[start]] -= 1
                start += 1
            end += 1
            maxLen = max(maxLen, end - start)
        return maxLen