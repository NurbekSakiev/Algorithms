# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def search(self, head, x):
	if not head:
    	return False
    if head.val == x:
        return True
    else:
        return self.search(head.next,x)