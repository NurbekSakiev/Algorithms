class Solution(object):
    def compareVersion(self, version1, version2):
        l1, l2 = version1.split('.'), version2.split('.')
        p1, p2 = 0, 0
        
        while p1 < len(l1) or p2 < len(l2):
            a = int(l1[p1]) if p1 < len(l1) else 0
            b = int(l2[p2]) if p2 < len(l2) else 0
            if a < b:
                return -1
            elif a > b:
                return 1
            p1 += 1
            p2 += 1
        return 0