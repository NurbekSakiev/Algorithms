class Solution(object):
    def multiply(self, num1, num2):
        
        res = [0  for i in range(len(num1) + len(num2))]
        
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                prod = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                sum = res[p2] + prod
                
                res[p1] += sum / 10
                res[p2] = sum % 10
        ptr = 0
        while ptr < len(res) and res[ptr] == 0:
            ptr += 1
        res = ''.join(map(str, res[ptr:]))
        return res if res != "" else "0"