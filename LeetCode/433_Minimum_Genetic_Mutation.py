class Solution(object):
    def minMutation(self, start, end, bank):
        q = [[start, 0]]
        minMutation = sys.maxint
        while q:
            curr = q.pop()
            currWord = curr[0]; currLen = curr[1]
            if currWord == end:
                minMutation = min(minMutation, currLen)
            for i in range(len(currWord)):
                part1, part2 = currWord[:i], currWord[i + 1:]
                for c in 'ACGT':
                    newWord = part1 + c + part2
                    if newWord in bank:
                        q.insert(0,[newWord, currLen + 1])
                        bank.remove(newWord)
        return -1 if minMutation == sys.maxint else minMutation