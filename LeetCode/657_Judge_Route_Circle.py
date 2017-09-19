class Solution(object):
    def judgeCircle(self, moves):
        x, y = 0, 0 
        for l in moves:
            if l == 'U':
                y += 1
            if l == 'D':
                y -= 1
            if l == 'R':
                x += 1
            if l == "L":
                x -= 1
        return x == 0 and y == 0