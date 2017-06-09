class Solution(object):
    def decodeString(self, s):
        
        if len(s) == 0:
            return ""
        st = []
        st.append(["",1])
        num = ""
        
        for i in s:
            if i.isdigit():
                num += i
            elif i == '[':
                st.append(["", int(num)])
                num = ""
            elif i == ']':
                char, val = st.pop()
                st[-1][0] += char*val
            else:
                st[-1][0] += i
            print st
            
        return st[0][0]