# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        if n == count:
            return head.next
        before = ListNode()
        before.next = head
        i = 0
        while i < count-n:
            before = before.next
            i += 1
        if before.next and before.next.next:
            before.next = before.next.next
            return head
        elif before.next:
            before.next = None
            return head
        else: return head.next

