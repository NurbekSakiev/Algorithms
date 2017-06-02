class Solution(object):
    def isValid(self, s):
        
        if len(s) < 1:
            return True
        if s[0] in ")}]" or len(s) % 2 != 0:
            return False
        st = []
        
        for i in s:
            if i in "({[":
                st.append(i)
            else:
                last = st[-1]
                if i == ')' and last == '(' or i == '}' and last == '{' or i == ']' and last == '[':
                    st.pop()
                else:
                    return False
        return len(st) == 0
        """
        :type s: str
        :rtype: bool
        """
        