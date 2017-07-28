# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        current = head
        firstEven, lastEven, firstOdd, lastOdd = None, None, None, None
        count = 1
        while current:
            if count % 2 == 0:
                if not firstEven:
                    firstEven = lastEven = current
                else:
                    lastEven.next = current
                    lastEven = lastEven.next
            else:
                if not firstOdd:
                    firstOdd = lastOdd = current
                else:
                    lastOdd.next = current
                    lastOdd = lastOdd.next
            count += 1
            current = current.next
        lastOdd.next = firstEven
        lastEven.next = None
        return firstOdd


# Solution 2


    def oddEvenList(self, head):
        if head:
            odd, evenHead  = head, head.next
            even = evenHead
            while even and even.next:
                odd.next = odd.next.next
                even.next = even.next.next
                odd = odd.next
                even = even.next
            odd.next = evenHead
        return head