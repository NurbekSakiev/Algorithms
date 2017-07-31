# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        carry = 0
        head = l3 = ListNode(0)
        
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            c = (a + b + carry) % 10
            carry = (a + b + carry) / 10
            if l1:
                l1.val = c
                l3.next = l1
                l1 = l1.next
            if l2:
                l2.val = c
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        if carry:
            node = ListNode(carry)
            l3.next = node
            
        return head.next