# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        start, end = head, head
        prevEnd = dummy
        while end:
            for _ in range(k-1):
                if end.next:
                    end = end.next
                else:
                    return dummy.next
            nextStart = end.next
            prev = prevEnd
            cur = start
            while cur != nextStart:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            start.next = nextStart
            prevEnd.next = end
            prevEnd = start
            start = start.next
            end = start
        return dummy.next


        
            


                
            


