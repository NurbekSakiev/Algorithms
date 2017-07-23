class Solution(object):
    def diffWaysToCompute(self, input):
        
        res = []
        for i in range(len(input)):
            if input[i] in '-+*':
                for p1 in self.diffWaysToCompute(input[:i]):
                    for p2 in self.diffWaysToCompute(input[i+1:]):
                        if input[i] == '+':
                            res.append(int(p1) + int(p2))
                        elif input[i] == '-':
                            res.append(int(p1) - int(p2))
                        elif input[i] == '*':
                            res.append(int(p1) * int(p2))
        
        if len(res) == 0:
            return([int(input)])
        return res