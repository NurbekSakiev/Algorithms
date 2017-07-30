class Solution(object):
    def isPalindrome(self, s):
        newStr = list(s.lower())
        j = 0
        for i in range(len(newStr)):
            if newStr[i].isalnum():
                newStr[j] = newStr[i]
                j += 1
        newStr = newStr[:j]
        start, end = 0, len(newStr) - 1
        while start < end:
            if newStr[start] != newStr[end]:
                return False
            start += 1
            end -= 1
        return True