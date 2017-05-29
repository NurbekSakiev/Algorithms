# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def removeElements(self, head, val):
        dummy = ListNode(0)
        newH = dummy
        
        while head:
            if head.val != val:
                dummy.next = head
                dummy = dummy.next
            head = head.next
            
        dummy.next = None
        return newH.next