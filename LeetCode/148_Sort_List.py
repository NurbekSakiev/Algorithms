# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        prev = None
        slow = fast = head
        
        while fast and fast.next:
            prev = slow 
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        l = self.sortList(head)
        r = self.sortList(slow)
        return self.merge(l,r)
        
    def merge(self, leftHead, rightHead):
        dummy = ListNode(0)
        nHead = dummy
        while leftHead or rightHead:
            if not leftHead:
                dummy.next = rightHead
                break
            elif not rightHead:
                dummy.next = leftHead
                break
            elif leftHead.val < rightHead.val:
                dummy.next = leftHead
                leftHead = leftHead.next
            else:
                dummy.next = rightHead
                rightHead = rightHead.next
            dummy = dummy.next
        return nHead.next
            
         
        