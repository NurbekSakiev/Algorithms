# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        count = 0 
        front = back = head
        if not head:
            return True
        while front:
            count += 1
            front = front.next
        front = head
        for i in range(count // 2):
            front = front.next
        prev = None
        while front:
            nxt = front.next
            front.next = prev
            prev = front
            front = nxt
        while prev and back:
            if prev.val != back.val:
                return False
            prev = prev.next
            back = back.next
        return True