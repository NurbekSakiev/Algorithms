class Solution(object):
    def findLongestWord(self, s, d):
        
        longest = ""
        for dictWord in d:
            i = 0
            for c in s:
                if i < len(dictWord) and dictWord[i] == c:
                    i += 1
            if i == len(dictWord) and len(dictWord) >= len(longest):
                if len(dictWord) > len(longest) or dictWord < longest:
                    longest = dictWord
        return longest