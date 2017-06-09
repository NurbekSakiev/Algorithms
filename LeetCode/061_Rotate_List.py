# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return
        nHead = tail = head
        count = 1
        
        while tail.next:
            tail = tail.next
            count += 1
        tail.next = head
        k %= count
        if k :
            for i in range(count - k):
                tail = tail.next
        nHead = tail.next
        tail.next = None
        return nHead
