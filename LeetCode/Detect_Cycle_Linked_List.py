# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        slow = fast = head
        isCycle = False
        while fast and slow:
            slow = slow.next
            if not fast.next:
                return None
            fast = fast.next.next
            if slow == fast:
                isCycle = True
                break
        if not isCycle:
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast