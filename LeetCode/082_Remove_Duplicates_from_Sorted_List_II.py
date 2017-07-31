# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return head
        nHead = ptr = ListNode(0)
        
        while head and head.next:
            current = head.val
            if head.next.val == current:
                while head and current == head.val:
                    head = head.next
            else:
                ptr.next = head
                head = head.next
                ptr = ptr.next
        if head:
            ptr.next = head
        else:
            ptr.next = None
        return nHead.next