low, maxLen = 0, 0
class Solution(object):
    def longestPalindrome(self, s):
        for i in range(len(s)):
            self.extend(s, i, i)
            self.extend(s, i, i+1)
        return s[low:low + maxLen]
    
    
    def extend(self, s, left, right):
        global maxLen, low
        while left >= 0 and right < len(s) and s[left] == s[right]:
            right += 1
            left -= 1
        if maxLen < right - left - 1:
            low = left + 1
            maxLen = right - left - 1