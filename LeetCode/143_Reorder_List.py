# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return head
        dummy = head
        slow = fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            fast = fast.next
        
        temp = slow.next
        slow.next = None
        slow = temp
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        while dummy.next:
            temp = dummy.next
            dummy.next = prev
            dummyPrev = prev.next
            dummy = temp
            prev.next = dummy
            prev = dummyPrev
        
        if prev:
            dummy.next = prev
            prev.next = None
        