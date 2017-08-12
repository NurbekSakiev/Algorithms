class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return head
        
        nHead = head
        
        while nHead.next:
            temp = nHead.next
            newNode = RandomListNode(nHead.label)
            nHead.next = newNode
            newNode.next = temp
            nHead = temp
        
        nHead = head
        
        while nHead:
            if nHead.random:
                nHead.next.random = nHead.random.next
            nHead = nHead.next.next
            
        nHead = head
        sHead = RandomListNode(0)
        secondHead = sHead
        
        while nHead :
            nxt = nHead.next.next
            
            copy = nHead.next
            sHead.next = copy
            sHead = sHead.next
            
            nHead.next = nxt
            nHead = nHead.next
            
        return secondHead.next