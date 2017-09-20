def rearrangeString(self, s):
        arr = [0 for i in range(26)]
        tot = 0
        newStr = ''
        for c in s:
            if 48 <= ord(c) <= 57:
                tot += int(c)
            else:
                arr[ord(c) - ord('A')] += 1
        
        
        for i in range(26):
            if arr[i] > 0:
                newStr += (arr[i] * chr(i + ord('A')))
        newStr += str(tot)
        
        return newStr