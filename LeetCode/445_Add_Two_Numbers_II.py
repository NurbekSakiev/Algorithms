# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s1 = []
        s2 = []
        carry = 0
        node = ListNode(0)
        
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        while s1 or s2:
            a = s1.pop() if s1 else 0
            b = s2.pop() if s2 else 0
            c = (a + b + carry) % 10
            carry = (a + b + carry) / 10
            node.val = c
            preNode = ListNode(0)
            preNode.next = node
            node = preNode
        if carry:
            node.val = carry
            return node
        else:
            return node.next