def decrypt(self, s, key):
        out = ''
        ptr = 0
        for char in s:
            if ptr == len(key): ptr = 0
            currKey = int(key[ptr])
            if char.isalpha():
                firstLetter = ord('A') if ord(char) < ord('Z') else ord('a')
                c = ord(char) - currKey
                if c < firstLetter:
                    c += 26
                char = chr(c)
                ptr += 1
            out += char
        return out