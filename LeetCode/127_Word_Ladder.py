class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        currLevel = []
        currLevel.append(beginWord)
        
        level = 1
        
        while currLevel:
            nextLevel = []
            level += 1
            while currLevel:
                currWord = currLevel.pop()
                arr = list(currWord)
                for i in range(len(currWord)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        temp = arr[i]
                        if arr[i] != c:
                            arr[i] = c
                        
                        newWord = ''.join(arr)
                        
                        if newWord == endWord and newWord in wordList:
                            return level
                        
                        if newWord in wordList:
                            nextLevel.append(newWord)
                            wordList.remove(newWord)
                            
                        arr[i] = temp
                    
            currLevel = nextLevel
                        
        return 0